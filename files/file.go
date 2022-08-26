
package main

import (
    "fmt"
    "os/exec"
    "math/rand"
    )


func colors() {
//         colorReset := "\033[0m"
    colorRed := "\033[31m"
colorGreen := "\033[32m"
colorYellow := "\033[33m"
colorBlue := "\033[34m"
colorPurple := "\033[35m"
colorCyan := "\033[36m"
colorWhite := "\033[37m"


        fmt.Println(string(colorRed), "You rock!")
        fmt.Println(string(colorGreen), "You are not supposed to hack me -_-")
        fmt.Println(string(colorYellow), "I only know how to declare variables in HTML")
        fmt.Println(string(colorBlue), "Shifted from Deb to Arch, planning for BSD")
        fmt.Println(string(colorPurple), "echo 'LEGENDZ NEVER DIE!'")
        fmt.Println(string(colorWhite), "All clear_!")
        fmt.Println(string(colorCyan), "You are good to go +_+")
        fmt.Println("next")
}


func main(){
    exec.Command("clear")
    colors()
    fmt.Println("Welcome abroad gentleman")
    var random = rand.Intn(100)
    var name = "S A A D - K H A N"
    var github = "Cyber-Diode"
    println("Name:~ " , name , "\nGithub:~ " , github)
    println("AGE:~ ", random)
    IDK_WHAT_IAM_DOING()
}

func IDK_WHAT_IAM_DOING(){
println("\nJust started learning GO, decided to share my knowledge. \nI guess this code can hack NASA WITH NO problem")
colorYellow := "\033[33m"
colorCyan := "\033[36m"
fmt.Println("The of  Value of PIE is 355/113 = " , 355 /113)
println(string(colorCyan),"Changed MY mind" )
println(string(colorYellow), "Just decided to complete 50 lines of code `+_+")


}
