



<template>
  <div id="app">
    <!-- Inicia la sección del Header -->

    <header>
      <a href="#" class="logo"><i class="fas fa-utensils"></i> RestaurantApp</a>
<!-- :class="isActive ? 'fa-times' : ''" @click.native="isActive = !isActive" -->
<!-- :class="isActive ? 'active' : '' " @click.native="isActive = !isActive" -->
      <div :class="isActive ? 'fa-times' : '' " @click.native="isActive = !isActive" id="menu-bar" class="fas fa-bars"></div>

      <nav :class="isActive ? 'active' : '' " @click.native="isActive = !isActive" class="navbar">
        <a href="#home">Home</a>
        <a href="#especialidad">Especialidad</a>
        <a href="#popular">Populares</a>
        <a href="#galeria">Galeria</a>
        <a href="#reseñas">Reseñas</a>
        <a href="#ordenar">Ordenar</a>
      </nav>
    </header>

    <!-- Finaliza la sección del Header -->

    <!-- Inicia la sección del Home -->

    <section class="home" id="home">
      <div class="content">
        <h3>La Respuesta al Apetito</h3>
        <p>
          Nuestro compromiso es que se te llene el apetito con los mejores
          platillos de toda la ciudad provenientes de los mejores restaurantes,
          una entrega a domicilio rápida y eficaz!
        </p>
        <a href="#ordenar" class="btn">¡Ordena Ahora!</a>
      </div>

      <div class="image">
        <img v-bind:src="require('./assets/home-img.png')" alt="Hamburguesa" />
        <!-- <img src="assets/home-img.png" alt="Hamburguesa"> -->
      </div>
    </section>

    <!-- Finaliza la sección del Home -->

    <!-- Inicia la sección de Especialidades -->

    <section class="especialidades" id="especialidad">
      <h1 class="heading">Nuestra <span>Especialidad</span></h1>

      <div class="box-container">
        <div class="box">
          <img
            class="image"
            v-bind:src="require('./assets/s-img-1.jpg')"
            alt="Hamburguesa"
          />

          <div class="content">
            <img
              v-bind:src="require('./assets/s-1.png')"
              alt="Icono Hamburguesa"
            />
            <h3>Deliciosa Hamburguesa Doble Queso</h3>
            <p>
              Pan Artesanal, lechuga y tomates organicos, elige tu carne
              favorita entre cerdo, milanesa o res, en su interior unas rodajas
              de queso cheddar ligeramente fundido, adiciona las salsas
              especiales de la casa
            </p>
          </div>
        </div>

        <div class="box">
          <img
            class="image"
            v-bind:src="require('./assets/s-img-2.jpg')"
            alt="Pizza"
          />
          <!-- <img v-bind:src="require('./assets/home-img.png')" alt="Hamburguesa"> -->

          <div class="content">
            <img v-bind:src="require('./assets/s-2.png')" alt="Icono Pizza" />
            <h3>Riquisima Pizza Familiar Italiana</h3>
            <p>
              Masa plana elaborada con harina de trigo, con salsa de tomate y
              queso, horneada a alta temperatura en un horno de leña para
              alcanzar una crocancia y dorado perfectos para delite del paladar.
            </p>
          </div>
        </div>

        <div class="box">
          <img
            class="image"
            v-bind:src="require('./assets/s-img-3.jpg')"
            alt="Helado"
          />

          <div class="content">
            <img v-bind:src="require('./assets/s-3.png')" alt="Icono Helado" />
            <h3>Cremoso Helado de Frambuesa</h3>
            <p>
              Helado artesanal elaborado con la receta especial que nos
              distingue. Elegimos personalmente las más rojas y deliciosas
              frambuesas, para deleitar tu paladar siempre con sabores
              especiales.
            </p>
          </div>
        </div>

        <div class="box">
          <img
            class="image"
            v-bind:src="require('./assets/s-img-4.jpg')"
            alt="Bebidas Tropicales"
          />

          <div class="content">
            <img v-bind:src="require('./assets/s-4.png')" alt="Icono Bebidas" />
            <h3>Frescas Bebidas Tropicales</h3>
            <p>
              Zumos de frutas tropicales, ricos en antioxidantes, retardan la
              oxidación celular y atenúan los síntomas de la vejez, alargando la
              expectativa de vida con la gran variedad de sabores de nuestro
              pais.
            </p>
          </div>
        </div>

        <div class="box">
          <img
            class="image"
            v-bind:src="require('./assets/s-img-5.jpg')"
            alt="Cookies"
          />

          <div class="content">
            <img v-bind:src="require('./assets/s-5.png')" alt="Icono Cook" />
            <h3>Sabrosa Cookie de Chocolate</h3>
            <p>
              La receta tradicional combina una masa a base de mantequilla y
              azúcar moreno o blanco con pepitas de chocolate semi-dulces
              encantando a grandes y chicos por igual a cualquier hora del día.
            </p>
          </div>
        </div>

        <div class="box">
          <img
            class="image"
            v-bind:src="require('./assets/s-img-6.jpg')"
            alt="Apetitoso Desayuno"
          />

          <div class="content">
            <img
              v-bind:src="require('./assets/s-6.png')"
              alt="Icono Desayuno"
            />
            <h3>Desayuno de Café y Croissant</h3>
            <p>
              Puedes encontrar desayunos sabrosos para compartirlos con personas
              especiales. En las mañanas disfrutarás de un irresistible
              croissant con queso acompañado del mejor café excelso Colombiano.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Finaliza la sección de Especialidades -->

<!-- Inicia la sección de Populares -->

      <section class="popular" id="popular">
        <h1 class="heading">La comida más <span>Popular</span></h1>

        <div class="box-container">
          <div class="box">
            <span class="precio">$15.000</span>
            <img
              class="image"
              v-bind:src="require('./assets/p-1.jpg')"
              alt="Hamburguesa Doble Carne"
            />
            <h3>Jugosa Hamburguesa Doble Carne</h3>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
            <a href="#" class="btn">Ordena Ahora!</a>
          </div>

          <div class="box">
            <span class="precio">$25.000</span>
            <img
              class="image"
              v-bind:src="require('./assets/p-2.jpg')"
              alt="Postre de Mandarina"
            />
            <h3>Delicioso Postre de Mandarina</h3>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
            <a href="#" class="btn">Ordena Ahora!</a>
          </div>

          <div class="box">
            <span class="precio">$10.000</span>
            <img
              class="image"
              v-bind:src="require('./assets/p-3.jpg')"
              alt="Pasabocas"
            />
            <h3>Sabrosos Pasabocas</h3>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star-half-alt"></i>
            </div>
            <a href="#" class="btn">Ordena Ahora!</a>
          </div>

          <div class="box">
            <span class="precio">$4.000</span>
            <img
              class="image"
              v-bind:src="require('./assets/p-4.jpg')"
              alt="Muffin Sabor Chocolate"
            />
            <h3>Encantadores Muffins Sabor Chocolate</h3>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star-half-alt"></i>
            </div>
            <a href="#" class="btn">Ordena Ahora!</a>
          </div>

          <div class="box">
            <span class="precio">$6.000</span>
            <img
              class="image"
              v-bind:src="require('./assets/p-5.jpg')"
              alt="Bebidas Tropicales"
            />
            <h3>Refrescantes Bebidas Tropicales</h3>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="far fa-star"></i>
            </div>
            <a href="#" class="btn">Ordena Ahora!</a>
          </div>

          <div class="box">
            <span class="precio">$4.000</span>
            <img
              class="image"
              v-bind:src="require('./assets/p-6.jpg')"
              alt="Helados de Frutos Rojos"
            />
            <h3>Exquisitos Helados de Frutos Rojos</h3>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="far fa-star"></i>
            </div>
            <a href="#" class="btn">Ordena Ahora!</a>
          </div>
        </div>
      </section>

      <!-- Finaliza la sección de Populares -->

    <!-- Inicia la sección de Paso a Paso -->

      <section class="pasoapaso">
        <div class="box">
          <img v-bind:src="require('./assets/step-1.jpg')" alt="" />
          <h3>Escoge tu Comida Favorita</h3>
        </div>

        <div class="box">
          <img v-bind:src="require('./assets/step-2.jpg')" alt="" />
          <h3>Entrega Rápida y Segura</h3>
        </div>

        <div class="box">
          <img v-bind:src="require('./assets/step-3.jpg')" alt="" />
          <h3>Metodos de Pago Sencillos</h3>
        </div>

        <div class="box">
          <img v-bind:src="require('./assets/step-4.jpg')" alt="" />

          <h3>Por Último, Disfruta tu Comida!!</h3>
        </div>
      </section>

      <!-- Finaliza la sección de Paso a Paso -->

    <!-- Inicia la sección de Galeria -->

      <section class="galeria" id="galeria">
        <h1 class="heading">Nuestra <span>Galeria</span> de Comidas</h1>

        <div class="box-container">
          <div class="box">
            <img v-bind:src="require('./assets/g-1.jpg')" alt="" />

            <div class="content">
              <h3>Jugosa Hamburguesa</h3>
              <p>
                Carne de ternera de alta calidad asada durante 3 ~ 4 minutos por
                cada una de sus caras conservando su jugosidad.
              </p>
              <a href="#" class="btn">Ordena Ahora!</a>
            </div>
          </div>

          <div class="box">
            <img v-bind:src="require('./assets/g-2.jpg')" alt="" />
            <div class="content">
              <h3>Frescos sándwiches</h3>
              <p>
                Jamón de primera calidad, rodeado del queso mas fresco! Perfecto
                para iniciar el día.
              </p>
              <a href="#" class="btn">Ordena Ahora!</a>
            </div>
          </div>

          <div class="box">
            <img v-bind:src="require('./assets/g-3.jpg')" alt="" />
            <div class="content">
              <h3>Burritos mexicanos</h3>
              <p>
                Deleita tu paladar con los mejores burritos mexicanos,
                acompañados de su característico y adictivo picante.
              </p>
              <a href="#" class="btn">Ordena Ahora!</a>
            </div>
          </div>

          <div class="box">
            <img v-bind:src="require('./assets/g-4.jpg')" alt="" />
            <div class="content">
              <h3>Cupcakes personalizables</h3>
              <p>
                Elige el que quieras, su sabor será inigualable, tanto que te
                hará comer hasta el papel
              </p>
              <a href="#" class="btn">Ordena Ahora!</a>
            </div>
          </div>

          <div class="box">
            <img v-bind:src="require('./assets/g-5.jpg')" alt="" />
            <div class="content">
              <h3>Cubitos de helado</h3>
              <p>
                El calor no seá problema si tienes varios de nuestros cubos de
                helado, te congelarán el cerebro
              </p>
              <a href="#" class="btn">Ordena Ahora!</a>
            </div>
          </div>

          <div class="box">
            <img v-bind:src="require('./assets/g-6.jpg')" alt="" />
            <div class="content">
              <h3>Presas de pollo brosterizadas</h3>
              <p>
                Si quieres 1 o si quieres 12, nuestras presas de pollo no tienen
                rival, atrevete a comer solo una
              </p>
              <a href="#" class="btn">Ordena Ahora!</a>
            </div>
          </div>

          <div class="box">
            <img v-bind:src="require('./assets/g-7.jpg')" alt="" />
            <div class="content">
              <h3>Desayuno inglés</h3>
              <p>
                Traido desde el otro lado del charco, el mas completo e
                inmejoable desayuno ingles en tu casa!
              </p>
              <a href="#" class="btn">Ordena Ahora!</a>
            </div>
          </div>

          <div class="box">
            <img v-bind:src="require('./assets/g-8.jpg')" alt="" />
            <div class="content">
              <h3>Galletas de chocolate con relleno</h3>
              <p>
                Un perfecto y pequeño postre tras un gran almuerzo, estas
                galletas te recargarán la energía
              </p>
              <a href="#" class="btn">Ordena Ahora!</a>
            </div>
          </div>

          <div class="box">
            <img v-bind:src="require('./assets/g-9.jpg')" alt="" />
            <div class="content">
              <h3>Pan con pasas</h3>
              <p>
                Si quieres llenarte y no tienes tiempo para una potente comida,
                la respuesta es este pan con pasas
              </p>
              <a href="#" class="btn">Ordena Ahora!</a>
            </div>
          </div>
        </div>
      </section>

      <!-- Finaliza la sección de Galeria -->

    <!-- Inicia la sección de Reseñas -->

      <section class="reseñas" id="reseñas">
        <h1 class="heading">Las <span>Reseñas</span> de Nuestros Clientes</h1>

        <div class="box-container">
          <div class="box">
            <img v-bind:src="require('./assets/pic1.webp')" alt="Cliente 1" />
            <h3>Hernán Crespo</h3>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
            <p>Excelente servicio, y precios comodos.</p>
          </div>

          <div class="box">
            <img v-bind:src="require('./assets/pic2.jpg')" alt="Cliente 2" />
            <h3>Marta Díaz</h3>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
            <p>
              Entrega del producto como aparece en la descripcion, ademas de que
              el pedido no demoró mucho en llegar.
            </p>
          </div>

          <div class="box">
            <img v-bind:src="require('./assets/pic3.jpg')" alt="Cliente 3" />
            <h3>Gustavo Fonte</h3>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
            <p>
              Pudimos disfrutar de la comida aun caliente sin salir de casa, muy
              bueno para esos días que se llega cansado del trabajo y no se
              quiere cocinar.
            </p>
          </div>
        </div>
      </section>

      <!-- Finaliza la sección de Reseñas -->

    <!-- Inicia la sección de Ordenar -->

    <section class="ordenar" id="ordenar">
      <h1 class="heading"><span>¡Ordena Ahora!</span></h1>

      <div class="row">
        <div class="image">
          <img v-bind:src="require('./assets/order-img.jpg')"
          alt="Mesera" />
        </div>

        <form action="">

          <div class="inputBox">
            <div class="row">

              <table class="table">
                <thead>
                  <th>Producto</th>
                  <th>Precio</th>
                  <th>Ordenar</th>              
                </thead>
                <tbody>
                  <tr v-for="producto in productos" v-bind:key="producto.url">
                    <td>{{producto.product_name}}</td>
                    <td>{{producto.product_price}}</td>
                    <td>
                      <button @click="getOneProduct(producto)" class="btn"><i class="fa fa-utensils"></i></button>
                    </td>
                  </tr>
                    <td>
                      <h3>Cantidad</h3>
                    </td>
                    <td>
                        <input type="number" v-model="pedidos.cantidad" placeholder="cant" />  
                    </td>
                  <tr>
                    
                  </tr>
                </tbody>
              </table>
            </div>

          </div>


          <div class="inputBox">
            <input type='hidden' v-model="clientes.url" placeholder='URL'>
            <input type="text" v-model="clientes.nombre" placeholder="Ingresa tu Nombre:" />
            <input type="text" v-model="clientes.apellido" placeholder="Ingresa tu Apellido:" />
            <input type="text" v-model="clientes.telefono" placeholder="Ingresa tu teléfono:" />
          </div>

          <textarea v-model="clientes.direccion" placeholder="Dirección:"></textarea>
          <textarea v-model="clientes.recomendaciones" placeholder="Recomendaciones:"></textarea>

          <input @click="postPedido" type="submit" value="¡Ordena Ahora!" class="btn" />
        </form>
      </div>
    </section>

    <!-- Finaliza la sección de Ordenar -->

    <!-- Inicia la sección del Footer -->

    <section id="footer" class="footer">
      <div class="share">
        <a href="#" class="btn">Facebook</a>
        <a href="#" class="btn">Twitter</a>
        <a href="#" class="btn">Instagram</a>
        <a href="#" class="btn">Pinterest</a>
        <a href="#" class="btn">Linkedin</a>
      </div>

      <h1 class="credit">
        Creado Por <span>El Grupo P50G4</span> | Todos los derechos reservados!.
      </h1>
    </section>

    <!-- Finaliza la sección del Footer -->

    <!-- Inicia el Botón de Scroll Top -->

    <a href="#home" class="fas fa-angle-up" id="scroll-top"></a>

    <!-- Finaliza el Botón de Scroll Top -->

    <!-- Inicia Loader -->

    <!-- :class="isActive ? 'fade-out' : '' " -->
    <!--  v-on:load=" document.querySelector('.loader-container').classList.add('fade-out')  " -->

    <div class="loader-container">

      <img src="./assets/loader.gif" alt="Loader" />
    
    </div>

    <!-- Finaliza el Loader -->

  </div>
</template>

<script>
import axios from "axios";

export default {

  data: function() {
    return {
      isActive: false,

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
      },

      pedidos:{
        cantidad: 0,
        producto: "",
        cliente: "",
      },

    };
  },

  mounted(){
    this.getClientes();
    this.getProductos();
  }, 

  components:{},

  methods: {

     getClientes(){
      axios.get('https://restaurantapp-be.herokuapp.com/clientes/')
      .then((result)=>{
        this.clientes = result.data;
      })
    },

    getProductos(){
      axios.get('https://restaurantapp-be.herokuapp.com/productos/')
      .then((result)=>{
        this.productos = result.data;
        this.productos.url = '';
      })
    },

    getOneProduct(producto){
      this.productos.url         = producto.url; 
      this.productos.producto    = producto.producto;
      this.productos.precio      = producto.precio;
      this.productos.tipo        = producto.tipo;

      this.pedidos.producto      = producto.url;
    },


    postPedido(){

        axios.post('https://restaurantapp-be.herokuapp.com/clientes/',
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
          alert("Registro Cliente correcto")
        })


        setTimeout(() => {
          
          axios.get('https://restaurantapp-be.herokuapp.com/clientes/')
          .then((result)=>{
            let id_cliente = result.data.length - 1
            let url_cliente = result.data[id_cliente].url
            this.pedidos.cliente = url_cliente
          })

        }, 2000);


        

        setTimeout(() => {

          axios.post('https://restaurantapp-be.herokuapp.com/pedido/',
          {
            pedido_cantidad: this.pedidos.cantidad,
            pedido_prducto:  this.pedidos.producto,
            pedido_cliente:  this.pedidos.cliente,
          },
          {auth:{
            username:'luis',
            password:'contraseña'
          }})
          .then(()=>{
            alert("Pedido realizado")
          })

        }, 4000);

    },

  },

}
</script>


<style>
@import url("https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600;700&display=swap");

:root {
  /* Variables en CSS */
  --coral: #ff7f50;
  --white: #fff;
  --gray: #666;
}

/* Sass -> Preprocesador para automatizar procesos y facilitar código
Como más tipos de variables, funciones (mixins), selectores anidados, herencia, etc. */

* {
  font-family: "Nunito", sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box; /* Manejar los contenedores de la maquetación */
  outline: none;
  border: none; /* Outline quita el contorno */
  text-decoration: none;
  /* text-transform: capitalize; */
  transition: all 0.2s linear; /* https://developer.mozilla.org/en-US/docs/Web/CSS/transition */
}

*::selection {
  background: var(--coral);
  color: var(--white);
}

/* Inicia Sección de Globales */

html {
  font-size: 62.5%; /* 1rem = 10px // Relativo -> Absoluto */
  overflow-x: hidden; /* Si sobresapasa un contenedor se oculta */
  scroll-behavior: smooth; /* Agrega animación ligera al realizar un Scroll */
  scroll-padding-top: 6rem; /* Agrega un padding cuando vamos a una sección */
}

body {
  background: #f7f7f7;
}

section {
  padding: 2rem 9%;
}

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
  font-weight: bold;
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

/* Finaliza Sección del Header */

/* Inicia Sección del Home */

.home {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  min-height: 100vh;
  align-items: center;
  background: url(./assets/home-bg.jpg) no-repeat;
  background-size: cover;
  background-position: center;
}

.home .content {
  flex: 1 1 40rem;
  padding-top: 6.5rem;
}

.home .image {
  flex: 1 1 40rem;
}

.home .image img {
  width: 100%;
  padding: 1rem;
  animation: float 3s linear infinite;
}

@keyframes float {
  /* Controla una secuencia de una animación */

  0%,
  100% {
    transform: translateY(0rem);
  }

  50% {
    transform: translateY(3rem);
  }
}

.home .content h3 {
  font-size: 5rem;
  color: #333;
}

.home .content p {
  font-size: 1.7rem;
  color: #666;
  padding: 1rem 0;
}

/* Finaliza Sección del Home */

/* Inicia Sección de Especialidades */

.especialidades .box-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.especialidades .box-container .box {
  flex: 1 1 30rem;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  border: 0.1rem solid rgba(0, 0, 0, 0.3);
  cursor: pointer;
  border-radius: 0.5rem;
}

.especialidades .box-container .box .image {
  height: 100%;
  width: 100%;
  object-fit: cover; /* https://developer.mozilla.org/es/docs/Web/CSS/object-fit */
  position: absolute;
  top: -100%;
  left: 0;
}

.especialidades .box-container .box .content {
  text-align: center;
  background: var(--white);
  padding: 2rem;
}

.especialidades .box-container .box .content img {
  margin: 1.5rem 0;
}

.especialidades .box-container .box .content h3 {
  font-size: 2.5rem;
  color: #333;
}

.especialidades .box-container .box .content p {
  font-size: 1.6rem;
  color: #666;
  padding: 1rem 0;
}

.especialidades .box-container .box:hover .image {
  top: 0;
}

.especialidades .box-container .box:hover .content {
  transform: translateY(100%);
}

/* Finaliza Sección de Especialidades */

/* Inicia la sección de Populares */

.popular .box-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.popular .box-container .box {
  padding: 2rem;
  background: var(--white);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  border: 0.1rem solid rgba(0, 0, 0, 0.3);
  border-radius: 0.5rem;
  text-align: center;
  flex: 1 1 30rem;
  position: relative;
}

.popular .box-container .box img {
  height: 25rem;
  object-fit: cover;
  widows: 100%;
  border-radius: 0.5rem;
}

.popular .box-container .box .precio {
  top: 3rem;
  left: 8.2rem;
  background: var(--coral);
  color: var(--white);
  font-size: 2rem;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  position: absolute;
}

.popular .box-container .box h3 {
  color: #333;
  font-size: 2.5rem;
  padding-top: 1rem;
}

.popular .box-container .box .stars i {
  color: gold;
  font-size: 2.5rem;
  padding: 1rem 0.1rem;
}

/* Finaliza la sección de Populares */

/* Inicia la sección de Paso a Paso */

.pasoapaso {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  padding: 1rem;
}

.pasoapaso .box {
  flex: 1 1 25rem;
  padding: 1rem;
  text-align: center;
}

.pasoapaso .box img {
  border-radius: 50%;
  border: 1rem solid var(--white);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
}

.pasoapaso .box h3 {
  font-size: 2.5rem;
  color: #333;
  padding: 1rem;
}

/* Finaliza la sección de Paso a Paso */

/* Inicia la sección de Galeria */

.galeria .box-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.galeria .box-container .box {
  height: 25rem;
  flex: 1 1 30rem;
  border: 1rem solid var(--white);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  border-radius: 0.5rem;
  position: relative;
  overflow: hidden;
}

.galeria .box-container .box img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}

.galeria .box-container .box .content {
  position: absolute;
  top: -100%;
  left: 0;
  height: 100%;
  width: 100%;
  background: rgba(255, 255, 255, 0.9);
  padding: 2rem;
  text-align: center;
}

.galeria .box-container .box h3 {
  font-size: 2.5rem;
  color: #333;
}

.galeria .box-container .box p {
  font-size: 1.5rem;
  color: #666;
  padding: 1rem 0;
}

.galeria .box-container .box:hover .content {
  top: 0;
}

/* Finaliza la sección de Galeria */

/* Inicia la sección de Reseñas */

.reseñas .box-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.reseñas .box-container .box {
  text-align: center;
  padding: 2rem;
  border: 1rem solid var(--white);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  border-radius: 0.5rem;
  flex: 1 1 30rem;
  background: #333;
  margin-top: 6rem;
}

.reseñas .box-container .box img {
  height: 12rem;
  width: 12rem;
  border-radius: 50%;
  border: 1rem solid var(--white);
  margin-top: -8rem;
  object-fit: cover;
}

.reseñas .box-container .box h3 {
  font-size: 2.5rem;
  color: var(--white);
  padding: 0.5rem 0;
}

.reseñas .box-container .box .stars i {
  font-size: 2rem;
  color: var(--coral);
  padding: 0.5rem 0;
}

.reseñas .box-container .box p {
  font-size: 1.7rem;
  color: #eee;
  padding: 1rem 0;
}

/* Finaliza la sección de Reseñas */

/* Inicia la sección de Ordenar */

.ordenar .row {
  padding: 2rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
  background: var(--white);
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  border-radius: 0.5rem;
}

.ordenar .row .image {
  flex: 1 1 30rem;
}

.ordenar .row .image img {
  height: 100%;
  width: 100%;
  object-fit: cover;
  border-radius: 0.5rem;
}

.ordenar .row form {
  flex: 1 1 50rem;
  padding: 1rem;
}

.ordenar .row form .inputBox {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.ordenar .row form .inputBox input,
.ordenar .row form textarea {
  padding: 1rem;
  margin: 1rem;
  font-size: 1.7rem;
  color: #333;
  text-transform: none;
  border: 0.1rem solid rgba(0, 0, 0, 0.3);
  border-radius: 0.5rem;
  width: 49%;
}

.ordenar .row form textarea {
  width: 100%;
  resize: none;
  height: 15rem;
}

.ordenar .row form .btn {
  background: none;
  margin-left: 1rem;
}

.ordenar .row form .btn:hover {
  background: var(--coral);
}

/* Finaliza Sección de Ordenar */

/* Inicia Sección del Footer */

.footer {
  background: #000;
  text-align: center;
}

.footer .share {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: center;
}

.footer .credit {
  padding: 2.5rem 1rem;
  color: var(--white);
  font-weight: normal;
  font-size: 2rem;
}

.footer .credit span {
  color: var(--coral);
}

/* Finaliza Sección del Footer */

/* Inicia el Botón de Scroll Top */

#scroll-top {
  position: fixed;
  top: 120%;
  right: 2rem;
  padding: 0.5rem 1.5rem;
  font-size: 4rem;
  background: var(--coral);
  color: var(--white);
  border-radius: 0.5rem;
  transition: 1s linear;
  z-index: 1000;
}

#scroll-top.active {
  top: calc(100% - 12rem);
}

/* Finaliza el Botón de Scroll Top */

/* Inicia el Loader */

.loader-container {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 10000;
  background: var(--white);
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}

.loader-container.fade-out {
  top: -120%;
}

/* Finaliza el Loader */

/* Media Queries */
/* Condicionales en CSS */

@media (max-width: 991px) {
  html {
    font-size: 55%;
  }

  header {
    padding: 2rem;
  }

  section {
    padding: 2rem;
  }
}

@media (max-width: 768px) {
  #menu-bar {
    display: initial;
  }

  header .navbar {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: #f7f7f7;
    border-top: 0.1rem solid rgba(0, 0, 0, 0.1);
    clip-path: polygon(0 0, 100% 0, 100% 0, 0 0);
    /* https://developer.mozilla.org/en-US/docs/Web/CSS/clip-path */
  }

  header .navbar.active {
    clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
  }

  header .navbar a {
    margin: 1.5rem;
    padding: 1.5rem;
    display: block;
    border: 0.2rem solid rgba(0, 0, 0, 0.1);
    border-left: 0.5rem solid var(--coral);
    background: #fff;
  }

  .popular .box-container .box .precio {
    top: 3rem;
    left: 23.8rem;
  }
}

@media (max-width: 450px) {
  html {
    font-size: 50%;
  }

  .popular .box-container .box .precio {
    top: 3.4rem;
    left: 3.4rem;
  }

  .ordenar .row form .inputBox input {
    width: 100%;
    margin-right: 0;
  }
}
</style>
