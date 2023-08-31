package server

import (
	"database/sql"
	"errors"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
	
	_ "github.com/lib/pq"
)

type Server struct {
	DB  *sql.DB
	Gin *gin.Engine
}

func (s *Server) InitDB() *Server {
	connStr := "user=" + os.Getenv("DB_USER") + " dbname=" + os.Getenv("DB_NAME") + " sslmode=disable"
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		panic(err)
	}
	// defer db.Close()

	// Test the connection
	err = db.Ping()
	if err != nil {
		panic(err)
	}
	s.DB = db
	fmt.Println("Connected to the database!")
	return s
}
func (s *Server) InitGin() *Server {
	g := gin.Default()
	s.Gin = g
	return s
}

func (s *Server) Ready() bool {
	return s.DB != nil && s.Gin != nil
}

func (s *Server) Start(ep string) error {
	if !s.Ready() {
		return errors.New("server isn't ready - make sure to init db and gin")
	}

	if err := http.ListenAndServe(ep, s.Gin.Handler()); err != nil {
		log.Fatal(err)
	}

	return nil
}

func (s *Server) RegisterRoutes() {
	s.Gin.POST("/books", s.HandleAddUser)
}
