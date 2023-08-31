package server

import "github.com/gin-gonic/gin"

type User struct{
	Password string `json:"password"`
	Email string `json:"email"`
	AcessToken string `json:"access_token"`
}

func (s *Server) HandleAddUser(ctx *gin.Context) {
	var user User
	err := ctx.BindJSON(&user)
	if err != nil{
		ctx.AbortWithError(400, err)
	}
	
}
