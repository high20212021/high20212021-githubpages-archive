#!/usr/bin/bash
echo "安装前预备"
echo "1.请勤更新脚本"
sleep 1
if ! command -v dialog &> /dev/null; then
    echo "脚本关键依赖项没有检查到：dialog"
    echo "请尝试：sudo apt install dialog"
    exit 1
fi
if ! command -v tar &> /dev/null; then
    echo "脚本关键依赖项没有检查到：tar"
    echo "请尝试：sudo apt install tar"
    exit 1
fi
if ! command -v axel &> /dev/null; then
    echo "脚本关键依赖项没有检查到：axel"
    echo "请尝试：sudo apt install axel"
    exit 1
fi
if ! command -v git &> /dev/null; then
    echo "脚本关键依赖项没有检查到：git"
    echo "请尝试：sudo apt install git"
    exit 1
fi
title="HighStudios WineArm-Installer v7.1"
options=(
    1 "安装系统预备"
    2 "安装架构转译框架"
    3 "安装Wine本体"
    4 "启动Wine-Arm"
    5 "更新脚本"
    6 "退出"
)
function function1() {
clear
sudo dpkg --add-architecture armhf
sudo apt update
sudo apt upgrade
sudo apt install cmake make gcc clang git wget nano neovim vim automake autoconf axel -y
sudo apt install zenity:armhf libegl-mesa0:armhf libgl1-mesa-dri:armhf libglapi-mesa:armhf libglx-mesa0:armhf libasound2:armhf libstdc++6:armhf libtcmalloc-minimal4:armhf gcc-arm-linux-gnueabihf sl:armhf -y
}
function build() {
clear
# git clone https://github.com/ptitSeb/box86
# git clone https://github.com/ptitSeb/box64
git clone https://gitea.com/high20212021/box86-mirror
git clone https://gitea.com/high20212021/box64-mirror
cd box86-mirror
mkdir build
cd build
cmake .. -DNOGIT=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DRPI4ARM64=ON
sudo make -j8
sudo make install
cd ..
cd ..
cd box64-mirror
mkdir build
cd build
cmake .. -DNOGIT=1 -DARM_DYNAREC=ON -DCMAKE_BUILD_TYPE=RelWithDebInfo
sudo make -j8
sudo make install
}
function getwin() {
clear
cd ..
cd ..
axel -n 128 https://www.playonlinux.com/wine/binaries/phoenicis/upstream-linux-amd64/PlayOnLinux-wine-6.14-upstream-linux-amd64.tar.gz
sudo tar xvf PlayOnLinux-wine-6.14-upstream-linux-amd64.tar.gz -C /usr
rm PlayOnLinux-wine-6.14-upstream-linux-amd64.tar.gz
mkdir wine32
axel -n 128 https://www.playonlinux.com/wine/binaries/phoenicis/upstream-linux-x86/PlayOnLinux-wine-7.0-rc4-upstream-linux-x86.tar.gz
tar xvf PlayOnLinux-wine-7.0-rc4-upstream-linux-x86.tar.gz -C ~/wine32
rm PlayOnLinux-wine-7.0-rc4-upstream-linux-x86.tar.gz
cd /usr/bin
ln -s ~/wine32/bin/wine wine32
cd ~/
}
function updatescpt() {
    rm install_wine.sh
    echo 将从官方源更新脚本
    axel -n 16 https://high20212021.github.io/install_wine.sh
    echo 更新完毕
}
function startwine() {
    clear
    echo "请在图形界面检查状态"
    export DISPLAY=:0
    box64 wine64 taskmgr
}
while true; do
    choice=$(dialog --clear --menu "$title" 0 0 0 "${options[@]}" 2>&1 >/dev/tty)
    case $choice in
        1)
            function1
            ;;
        2)
            build
            ;;
        3)
            getwin
            ;;
        4)
            startwine
            ;;
        5)
            updatescpt
            ;;
        6)
            break
            ;;
        *)
            echo "无效选项，请重新输入"
            ;;
    esac
done


