#!/bin/bash

remove_pyc()
{
    py_files=$(ls *.py 2> /dev/null | wc -l)
    pyc_files=$(ls *.pyc 2> /dev/null | wc -l)
    if [ "0" != "$py_files" ];
    then
        chmod +x *.py
    fi

    if [ "0" != "$pyc_files" ];
    then
        rm *.pyc 
    else
        return 
    fi
}

clean()
{
    for file in `ls $1`
        do
            if [ -d $file ];
            then
                echo $PWD
                OLDPWD=$PWD
                echo $file
                cd $file
                remove_pyc
                clean "."
                cd $OLDPWD
            else 
                remove_pyc
            fi
        done
}

#if [ $# -gt 0 ];
#then
#    clean "$1"
#else
#    python -m compileall .
#    clean "."
#fi
chmod +x `find . -name '*.py'`
rm `find . -name '*.pyc'`
