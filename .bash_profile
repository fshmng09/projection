# .bashrcの実行（存在する場合）
if [ -f ~/.bashrc ]; then
  . ~/.bashrc
fi

# 環境変数の設定
# パス
#export PATH=$PATH:コマンド検索パス

#alias エイリアス="実行するファイル"

alias mon2F="rsync -auv --delete nakano@172.16.31.67:/home/nakano/fushiming/ /Users/fushiming/share/monbetsu"
alias F2mon="rsync -auv --delete /Users/fushiming/share/monbetsu/ nakano@172.16.31.67:/home/nakano/fushiming "
alias jn="jupyter notebook"
alias jn_lim="jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10"
alias e='emacsclient -nw -a ""'
alias e_kill='emacsclient -e "(kill-emacs)"'
alias lmk='latexmk -pvc'
alias lmkc='latexmk -c'
alias updatedb='sudo /usr/libexec/locate.updatedb'
alias download_site="wget -r -l inf -p -k -w 1 "
alias brew="env PATH=${PATH/\/Users\/fushiming\/\.pyenv\/shims:/} brew"

#ofp
alias ofp2local="rsync -auv --delete t00435@ofp.jcahpc.jp:/home/t00435/imac/ /Users/fushiming/ofp/"
alias loca2ofp="rsync -auv --delete /Users/fushiming/ofp t00345@ofp.jcahpc.jp:/home/t00435/imac/"

#server
alias sshatom='ssh -Y fushimi@157.82.253.150'
alias sshclione='ssh -Y fushimi@172.16.31.40'
alias sshbambi='ssh -Y fushimi@172.16.31.12'
alias sshocha='ssh -Y fushimi@172.16.31.11'
alias sshmonbetsu='ssh -Y nakano@172.16.31.67'

#python
alias fushiming="source ~/pymodules/env/bin/activate"

export LANG=ja_JP.UTF-8;
export LESSCHARSET=utf-8;

export PATH=/usr/local/bin:$PATH


# MacPorts Installer addition on 2016-12-29_at_23:38:21: adding an appropriate PATH variable for use with MacPorts.
export PATH="/opt/local/bin:/opt/local/sbin:$PATH"
# Finished adapting your PATH environment variable for use with MacPorts.


#pyenv options
#export PYENV_ROOT="${HOME}/.pyenv"
#export PATH="${PYENV_ROOT}/bin:$PATH"
#export PATH="$HOME/.pyenv/shims:$PATH"
#eval "$(pyenv init -)"

#export PATH="$HOME/.pyenv/shims:$PATH"
export PATH=$HOME/.nodebrew/current/bin:$PATH
export JAVA_HOME=$(/usr/libexec/java_home)
export STUDIO_JDK=${JAVA_HOME%/*/*}

#gdal
export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH


# 2018年 4月27日 金曜日 03時31分42秒 UTC - MODIS Reprojection Swath Tool modifications
MRTSWATH_HOME="/Users/fushiming/Downloads/MRTSwath_download_Mactel/MRTSwath"
PATH="$PATH:/Users/fushiming/Downloads/MRTSwath_download_Mactel/MRTSwath/bin"
MRTSWATH_DATA_DIR="/Users/fushiming/Downloads/MRTSwath_download_Mactel/MRTSwath/data"
export MRTSWATH_HOME PATH MRTSWATH_DATA_DIR
export PYTHONPATH="~/pymodules:$PYTHONPATH"

export ANDROID_HOME=“/usr/local/share/android-sdk”
export PATH=“${PATH}:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools”


#basemap
export GEOS_DIR=/usr/local/Cellar/geos/3.7.1/　

#multiprocessing
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

#llvm
export PATH="/usr/local/opt/llvm/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/llvm/lib"
export CPPFLAGS="-I/usr/local/opt/llvm/include"

#gcc
export CC=gcc
export CXX=gcc
export ARCHFLAGS="-arch x86_64"
