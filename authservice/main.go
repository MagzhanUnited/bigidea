package main

import (
	"fmt"

	"github.com/acheong08/OpenAIAuth/auth"
)

func main() {
	auth := auth.NewAuthenticator("nurlannurlanov612@gmail.com", "magzhan2005", "https://8.219.5.240:8060")
	err := auth.Begin()
	if err.Error != nil {
		println("Error: " + err.Details)
		println("Location: " + err.Location)
		println("Status code: " + fmt.Sprint(err.StatusCode))
		println("Embedded error: " + err.Error.Error())
		return
	}
	token := auth.GetAccessToken()
	fmt.Println(token)
}
