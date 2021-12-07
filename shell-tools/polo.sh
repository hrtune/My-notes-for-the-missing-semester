# !/bin/bash

polo(){
    cd $(cat /tmp/marco.txt) || echo 'Marco first.'
}

polo
