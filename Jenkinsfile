properties([pipelineTriggers([pollSCM('* * * * * ')])])
node {
    stage ("one"){
        git "https://github.com/ERAN1202/python_digital_net4u.git"
    }
    stage ("two"){
        bat "dir"
    }
}
