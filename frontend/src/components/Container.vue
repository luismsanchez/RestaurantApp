<template>
  <div class="row d-block">
    <div class="col-lg-6 mb-5">
      <a href="#" class="logo"
          ><i class="fas fa-utensils"></i> RestaurantApp</a
        >

        <div id="menu-bar" class="fas fa-bars"></div>

        <nav class="navbar">
          <a href="#clientes">Clientes</a>
          <a href="#productos">Productos</a>
        </nav>
    </div>
    <div class="col-lg-6 mb-5">
      <h1 class="lg-6 mb-5">Clientes</h1>
      <input type='hidden' v-model="clientes.url" class="form-control mt-2" placeholder='URL'>
      <input type='text' v-model="clientes.nombre" class="form-control mt-2" placeholder='Nombre'>
      <input type='text' v-model="clientes.apellido" class="form-control mt-2" placeholder='Apellido'>
      <input type='text' v-model="clientes.telefono" class="form-control mt-2" placeholder='Teléfono'>
      <input type='text' v-model="clientes.direccion" class="form-control mt-2" placeholder='Dirección'>
      <input type='text' v-model="clientes.recomendaciones" class="form-control mt-2" placeholder='Recomendaciones'>
      <button @click="postCliente" class="btn btn-block btn-success mt-2">Guardar</button>
    </div>

    <div class="col-lg-6 mb-5">
      <table class="table">
        <thead>
          <th>URL</th>
          <th>Nombre</th>
          <th>Apellido</th>
          <th>Telefono</th>
          <th>Direccion</th>
          <th>Recomendaciones</th>
          <th>Edit</th>
          <th>Delete</th>
        </thead>
        <tbody>
          <tr v-for="cliente in clientes" v-bind:key="cliente.url">
            <td>{{cliente.url}}</td>
            <td>{{cliente.cli_nombre}}</td>
            <td>{{cliente.cli_apellido}}</td>
            <td>{{cliente.cli_celular}}</td>
            <td>{{cliente.cli_direccion}}</td>
            <td>{{cliente.cli_recomendaciones}}</td>
            <td>
              <button @click="getOne(cliente)" class="btn bn-sm btn-success"><i class="fa fa-pencil"></i></button>
            </td>
            <td>
              <button @click="deleteOne(cliente.url)" class="btn bn-sm btn-success"><i class="fa fa-trash"></i></button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="col-lg-6 mb-5">
      <h1 class="lg-6 mb-5">Productos</h1>
      <input type='hidden' v-model="productos.url" class="form-control mt-2" placeholder='URL'>
      <input type='text' v-model="productos.producto" class="form-control mt-2" placeholder='Producto'>
      <input type='text' v-model="productos.precio" class="form-control mt-2" placeholder='Precio'>
      <input type='text' v-model="productos.tipo" class="form-control mt-2" placeholder='Tipo'>
      <button @click="postProducto" class="btn btn-block btn-success mt-2">Guardar</button>
    </div>

    <div class="col-lg-6 mb-5">
      <table class="table">
        <thead>
          <th>URL</th>
          <th>Producto</th>
          <th>Precio</th>
          <th>Tipo</th>
          <th>Edit</th>
          <th>Delete</th>
        </thead>
        <tbody>
          <tr v-for="producto in productos" v-bind:key="producto.url">
            <td>{{producto.url}}</td>
            <td>{{producto.product_name}}</td>
            <td>{{producto.product_price}}</td>
            <td>{{producto.product_tipo}}</td>
            <td>
              <button @click="getOneProduct(cliente)" class="btn bn-sm btn-success"><i class="fa fa-pencil"></i></button>
            </td>
            <td>
              <button @click="deleteOneProduct(cliente.url)" class="btn bn-sm btn-success"><i class="fa fa-trash"></i></button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

</template>

<script>
import axios from 'axios'

export default {

  name: 'Container',
  props: {
    msg: String
  },
  data(){
    return{
      clientes:{ 
        url: "",
        nombre: "",
        apellido: "",
        telefono: 0,
        direccion: "",
        recomendaciones: "",
      },
      productos:{
        url:"",
        producto: "",
        precio: 0,
        tipo: "",
      }
    }
  },
  mounted(){
    this.getClientes();
    this.getProductos();
  },
  methods:{
    getClientes(){
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
    },

    postCliente(){
      if(this.clientes.url == ''){
        axios.post('http://localhost:8000/clientes/',
        {
          cli_nombre: this.clientes.nombre,
          cli_apellido: this.clientes.apellido,
          cli_celular: this.clientes.telefono,
          cli_direccion: this.clientes.direccion,
          cli_recomendaciones: this.clientes.recomendaciones,
        },
        {auth:{
          username:'luis',
          password:'contraseña'
        }})
        .then(()=>{
          this.getClientes();
        })
      } else {
        axios.put(this.clientes.url,
        {
          cli_nombre: this.clientes.nombre,
          cli_apellido: this.clientes.apellido,
          cli_celular: this.clientes.telefono,
          cli_direccion: this.clientes.direccion,
          cli_recomendaciones: this.clientes.recomendaciones,
        },
        {auth:{
          username:'luis',
          password:'contraseña'
        }})
        .then(()=>{
          this.getClientes();
        })
      }
    },

    
  }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600;700&display=swap");



.heading {
  text-align: center;
  font-size: 3.5rem;
  padding: 1rem;
  color: var(--gray);
}

.heading span {
  color: var(--coral);
}

.btn {
  display: inline-block;
  padding: 0.8rem 3rem;
  border: 0.2rem solid var(--coral);
  color: var(--coral);
  cursor: pointer;
  font-size: 1.7rem;
  border-radius: 0.5rem;
  position: relative;
  overflow: hidden;
  z-index: 0;
  margin-top: 1rem;
}

.btn::before {
  /* PseudoElemento (hijo) que agrega contenido estético */
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 0%;
  height: 100%;
  background: var(--coral);
  transition: 0.3s linear;
  z-index: -1;
  /* border-radius: 1rem; */
}

.btn:hover::before {
  width: 100%;
  left: 0;
}

.btn:hover {
  color: var(--white);
}

/* Finaliza Sección de Globales */

/* Inicia Sección del Header */

header {
  position: fixed; /* Al darle scroll el nav se queda fijo */
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000; /* https://developer.mozilla.org/en-US/docs/Web/CSS/z-index */
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--white);
  padding: 2rem 9%;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
}

header .logo {
  font-size: 2.5rem;
  font-weight: bolder;
  color: var(--gray);
}

header .logo i {
  padding-right: 0.5rem;
  color: var(--coral);
}

header .navbar a {
  font-size: 2rem;
  margin-left: 2rem;
  color: var(--gray);
}

header .navbar a:hover {
  /* PseudoClase - Altera el Aspecto de un Elemento */
  color: var(--coral);
  /*font-weight: bold;*/
}

#menu-bar {
  font-size: 3rem;
  cursor: pointer;
  color: var(--gray);
  border: 0.1rem solid var(--gray);
  border-radius: 0.3rem;
  padding: 0.5rem 1.5rem;
  display: none;
}


</style>
