properties([parameters([string(defaultValue: 'Eran', description: 'What is your name?', name: 'NAME')]), pipelineTriggers([pollSCM('* * * * * ')])])
node {
    stage ("clone"){
        git "https://github.com/ERAN1202/python_digital_net4u.git"
    }
    stage ("showdir"){
        bat "dir"
    }
}
