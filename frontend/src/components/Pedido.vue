<template>
<div id="app">
  <div class="Ordenar">

    <h1 class="title">¡Ordena Ahora!</h1>
    
    <form action class="form" @submit.prevent="OrdenarAhora">
      <label class="form-label" for="#fecha">Fecha:</label>
      <input v-model="pedidos.fecha" class="form-input" type="fecha" id="fecha" placeholder="Fecha">
      <label class="form-label" for="#cantidad">Cantidad:</label>
      <input v-model="pedidos.cantidad" class="form-input" type="cantidad" id="cantidad" placeholder="Cantidad">
      <label class="form-label" for="#producto">Producto:</label>
      <input v-model="pedidos.producto" class="form-input" type="producto" id="producto" placeholder="Producto">
      <input class="form-submit" type="submit" value="Ordenar">
    </form>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {

  name: 'Pedido',
  props: {
    msg: String
  },
  data(){
    return{
      pedidos:{
        fecha: "",
        cantidad: 0,
        producto: ""
      }
    }
  },

  mounted(){},

  methods:{
    /* getClientes(){
      axios.get('http://localhost:8000/clientes/')
      .then((result)=>{
        this.clientes = result.data;
        this.clientes.url = '';
      })
    },
    getProductos(){
      axios.get('http://localhost:8000/productos/')
      .then((result)=>{
        this.productos = result.data;
        this.productos.url = '';
      })
    },
    getOne(cliente){
      this.clientes.url       = cliente.url; 
      this.clientes.nombre    = cliente.cli_nombre;
      this.clientes.apellido  = cliente.cli_apellido;
      this.clientes.telefono  = cliente.cli_celular;
      this.clientes.direccion = cliente.cli_direccion;
      this.clientes.recomendaciones = cliente.cli_recomendaciones;
      
    },
    deleteOne(url){
      axios.delete(url,{auth:{
        username:'luis',
        password:'contraseña'
      }})
      .then(()=>{
        this.getClientes();
      })
    },

    getOneProduct(producto){
      this.productos.url         = producto.url; 
      this.productos.producto    = producto.producto;
      this.productos.precio      = producto.precio;
      this.productos.tipo        = producto.tipo;
    },
    deleteOneProduct(url){
      axios.delete(url,{auth:{
        username:'luis',
        password:'contraseña'
      }})
      .then(()=>{
        this.getProductos();
      })
    }, */

    OrdenarAhora(){
        axios.post('http://localhost:8000/pedido/',
        {
          pedido_fecha: this.pedidos.fecha,
          pedido_cantidad: this.pedidos.cantidad,
          pedido_prducto: this.pedidos.producto,
        },
        {auth:{
          username:'luis',
          password:'contraseña'
        }})
        .then(()=>{
          alert("Pedido realizado")
        })
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
