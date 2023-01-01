try:
    from os import system
    from subprocess import check_output
    from rich.console import Console
except ImportError:
    print("Dependencies not found so installing them")
    prcs = system("pacman -S python-rich")
    if prcs != 0 :
        print("Dependencies failed to install")
        exit(prcs)
    else:
        from rich.console import Console
        pass

console = Console()

step1pass = False
step2pass = False
step3pass = False

console.print("Welcome to [blue]Arnix OS[/blue] Installer")

console.print("Lets get started")
console.log("[[yellow]Step 1:-[/yellow] Partition disks...]")

def usercheck():
    user = check_output("whoami")
    if user != b'root\n':
        print("You are not root so exiting")
        exit(1)
    else:
        pass

def partitioning():
    global step1pass , biostype , device
    console.print("[yellow]Creating partitons...")
    console.print("Take a look at the drives to partiton..")
    system("lsblk")

    device = input("Enter the storage device to partiton:- ")
    if device == None:
        print("No input detected")
        exit(1)
    else:
        pass
    console.print("[green]> loading cfdisk.[/green]")
    cfdiskprcs = system(f"cfdisk {device}")

    if cfdiskprcs != 0:
        console.print("[red]error:-[/red] cfdisk process did not exited currectly")
        exit(cfdiskprcs)
    else:
        biostype = int(input('Enter the type of bios of your pc:- \n 1.EFI \n 2.MBR \n Enter 1 or 2 for BIOS type:- '))

        if biostype == int(1):
            print("View the partitons:- ")
            system('lsblk')
            choice = input("Enter the main partition? ")
            console.print(f"[green]> loading mkfs.ext4[/green]")
            prcs = system(f"mkfs.ext4 {choice}")
            if prcs != 0:
                console.print(f"[red]error:-[/red] mkfs.ext4 exited with {prcs} as exit code..")
                exit(prcs)
            else:
                system(f"mount {choice} /mnt")
                system("mkdir /mnt/boot")
                bootpart = input("Enter boot partiton:- ")
                console.print("[green]> making boot partition[/green]")
                prcs1 = system(f'mkfs.fat -F32 {bootpart}')
                if prcs1 != 0:
                    console.print(f"[red]error[/red] process exited with {prcs1} as exit code..")
                    exit(prcs1)
                else:
                    system(f"mount {bootpart} /mnt/boot")
                    console.print('[yellow]congrats:-[/yellow] Step 1:- Partitioning Done')
                    step1pass = True
                    basestrap()

        elif biostype == int(2):
            print("View the partitions:-")
            system("lsblk")
            choice = input("Enter the main partition? ")
            console.print(f"[green]> loading mkfs.ext4[/green]")
            prcs = system(f"mkfs.ext4 {choice}")
            if prcs != 0 :
                console.print(f"[red]error:- [/red] process exited with {prcs} with exit code")
                exit(prcs)
            else:
                bootpart = input(f"Enter the boot partition? ")
                console.print(f"[green]> making boot partition[/green]")
                prcs1 = system(f"mkfs.fat -F32 {bootpart}")
                if prcs1 != 0:
                    console.print(f"[red]error[/red] process exited with {prcs1} as exit code..")
                    exit(prcs1)
                else:
                    system(f"mount {choice} /mnt")
                    console.print('[yellow]congrats:-[/yellow] Step 1:- Partitioning Done')
                    step1pass = True
                    basestrap()

        else:
            console.print("[red]error:-[/red] invalid input")
            exit(2)

def basestrap():
    global step2pass
    console.log("[[yellow]Step 2:-[/yellow] Bootstrapping the system...]")
    console.print("[green]> running pacstrap... [/green]")
    if biostype == 2:
        basestp = system("pacstrap /mnt archlinux-keyring base base-devel linux linux-firmware linux-headers vim nano networkmanager grub")
        pass
    else:
        basestp = system("pacstrap /mnt archlinux-keyring base base-devel linux linux-firmware linux-headers vim nano networkmanager grub efibootmgr")
        pass

    if basestp != 0:
        console.print("[red]error:- [/red] bootstapping system failed..")
        exit(basestp)
    else:
        console.print('[yellow]congrats:-[/yellow] Step 2:- Bootstrapping Done')
        step2pass = True
        poststrap()

def poststrap():
    global step3pass
    console.log("[[yellow]Step 3:-[/yellow] Configuring your system..]")
    username = input("Enter your user name? ")
    print("Showing list of timezones..")
    system("timedatectl list-timezones")
    tzone = input("Enter your timezone? ")

    console.print("running some commands..")
    prcs = system(f"arch-chroot /mnt useradd -m {username}")
    if prcs != 0:
        console.print(f"[red]error:-[/red] process exited with exit code {prcs}")
        exit(prcs)
    else:
        prcspwd = system(f"arch-chroot /mnt passwd {username} && exit")
        if prcspwd == 0:
            prcs2 = system(f"arch-chroot /mnt ln -sf /etc/localtime /usr/share/zoneinfo/{tzone} && exit")
            if prcs2 != 0:
                console.print(f"[red]error:-[/red] process exited with exit code {prcs2}")
                exit(prcs2)
            else:
                console.print("[green]> running mkinitcpios..[/green]")
                prcs3 = system("arch-chroot /mnt mkinitcpio -p linux && exit")
                if prcs3 != 0:
                    console.print(f"[red]error:-[/red] process exited with exit code {prcs3}")
                    exit(prcs3)
                else:
                    console.print(f"> [green]> running grub install..")
                    if biostype == 2:
                        prcs4 = system(f"arch-chroot /mnt grub-install {device}")
                        if prcs4 != 0:
                            console.print("[red]error:-[/red] grub failed to install")
                            exit(prcs4)
                        else:
                            prcsgbcfg = system("arch-chroot /mnt grub-mkconfig -o /boot/grub/grub.cfg")
                            if prcsgbcfg == 0:
                                prcs5 = system("genfstab /mnt >> /mnt/etc/fstab")
                                if prcs5 != 0:
                                    print("fstab generation failed..")
                                    exit(prcs5)
                                else:
                                    print("Arnix OS has installed sucessfully.. now reboot your PC.")
                                    step3pass = True
                            else:
                                print("configuring grub failed.")
                    elif biostype == 1:
                        prcs4 = system(f"arch-chroot grub-install {device} --target=x86_64-efi --efi-directory=/boot --bootloader-id=ArnixOS231 && grub-mkconfig -o /boot/grub/grub.cfg && exit")
                        if prcs4 != 0:
                            console.print("[red]error:-[/red] grub failed to install")
                            exit(prcs4)
                        else:
                            prcs5 = system("genfstab /mnt >> /mnt/etc/fstab")
                            if prcs5 != 0:
                                print("fstab generation failed..")
                                exit(prcs5)
                            else:
                                print("Arnix OS has installed sucessfully.. now reboot your PC.")
                                step3pass = True
        else:
            console.print("[red]error:-[/red] passwd failed..")
            exit(prcspwd)

usercheck()
partitioning()
