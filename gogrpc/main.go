package main

import (
	"gogrpc/server"
	"log"
	"os"

	"github.com/joho/godotenv"
)

func main() {
	// srv := &api.Server{}
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}
	srv := server.Server{}
	srv.InitDB()
	srv.InitGin()

	srv.RegisterRoutes()

	srv.Start(":" + os.Getenv("PORT"))
}
