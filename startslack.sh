#!/data/data/com.termux/files/usr/bin/bash
if [ ! -d "/data/data/com.termux/files/home/slackware" ];then
  echo 检测到Slackware文件夹不存在，即将为你安装Slackware
  mkdir slackware
  apt install proot wget
  cd slackware
  wget https://mirrors.tuna.tsinghua.edu.cn/slackwarearm/slackwarearm-devtools/minirootfs/roots/slackaarch64-current-miniroot_08Sep23.tar.xz
  proot --link2symlink tar -xvf slackaarch64-current-miniroot_08Sep23.tar.xz --exclude=dev||:
  rm slackaarch64-current-miniroot_08Sep23.tar.xz
  cd ~/
fi
cd $(dirname $0)
unset LD_PRELOAD
command="proot"
command+=" --link2symlink"
command+=" -0"
command+=" -r slackware"
command+=" -b /dev"
command+=" -b /proc"
command+=" -b slackware/root:/dev/shm"
command+=" -w root"
command+=" /usr/bin/env -i"
command+=" HOME=/root"
command+=" PATH=/usr/local/sbin:/usr/local/bin:/bin:/usr/bin:/sbin:/usr/sbin:/usr/games:/usr/local/games"
command+=" TERM=$TERM"
command+=" LANG=C.UTF-8"
command+=" /bin/bash --login"
echo Slackware ARM
exec $command
