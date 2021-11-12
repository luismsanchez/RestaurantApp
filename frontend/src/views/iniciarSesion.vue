<template>
<div id="app">
  <div class="login">

    <h1 class="title">Iniciar Sesión Administrador</h1>
    
    <form action class="form" @submit.prevent="LogInUser">
      <label class="form-label" for="#user">Usuario:</label>
      <input v-model="user.username" class="form-input" type="user" id="user" required placeholder="Usuario">
      <label class="form-label" for="#password">Password:</label>
      <input v-model="user.password" class="form-input" type="password" id="password" placeholder="Password">
      <p v-if="error" class="error">Las credenciales no son correctas</p>
      <input class="form-submit" type="submit" value="Login">
<!--       <button @click="LogInUser" class="btn btn-block btn-success mt-2">Iniciar Sesión</button> -->    </form>
    
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {

  name: 'iniciarSesion',
  props: {
    msg: String
  },
  data(){
    return{
      user:{ 
        url: "",
        username: "",
        password: "",
      }
    }
  },
  mounted(){},
  methods:{
    login() {
      console.log(this.user.username);
      console.log(this.user.password);
    },
    LogInUser: function(){
            axios.post(
                "http://127.0.0.1:8000/api-auth/login/", 
                {
                    username: this.user.username,
                    password: this.user.password,
                },
                {auth:{
                  username:'luis',
                  password:'contraseña'
                }}
                )
                .then((res) => {
                    console.log(res.data);
                    //this.$emit('completedLogIn', dataLogIn)
                })
                .catch((error) => {
                    
                    if (error.response.status == "401")
                        alert("ERROR 401: Credenciales Incorrectas.");
                    
                });
    },
  }
}
</script>

<style scoped>
.login {
  padding: 2rem;
}
.title {
  text-align: center;
}
.form {
  margin: 3rem auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 20%;
  min-width: 350px;
  max-width: 100%;
  background: rgba(23, 28, 32, 0.9);
  border-radius: 5px;
  padding: 40px;
  box-shadow: 0 4px 10px 4px rgba(0, 0, 0, 0.3);
}
.form-label {
  margin-top: 2rem;
  color: white;
  margin-bottom: 0.5rem;
  /* &:first-of-type {
    margin-top: 0rem;
  } */
}
.form-input {
  padding: 10px 15px;
  background: none;
  background-image: none;
  border: 1px solid white;
  color: white;
 /*  &:focus {
    outline: 0;
    border-color: #1ab188;
  } */
}
.form-submit {
  background: coral;
  border: none;
  color: white;
  margin-top: 3rem;
  padding: 1rem 0;
  cursor: pointer;
  transition: background 0.2s;
 /*  &:hover {
    background: #0b9185;
  } */


}
</style>