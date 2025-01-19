<template>
  <head>
      <link rel="stylesheet" href="style.css"/>
 </head>
  <body>
      <div class="receipt">

  <p class="greeting"> Thank you for your order! </p>

  <!-- Order info -->
  <div class="order">

    <p> Order No : 8821920579 </p>
    <p> Date : 2023/11/28 </p>
    <p> Theater: Auditorium 1 </p>

  </div>

  <hr>

  <!-- Details -->
  <div class="details">

    <h3> Details </h3>

    <div class="product">
      <img src="https://i.ebayimg.com/images/g/cQoAAOSwawplJYwf/s-l1200.jpg" alt="">

      <div class="info">

        <h4> TAYLOR SWIFT THE ERAS TOUR  </h4>

        <p> Seats: 10-1, 10-2 </p>
        <p> Qty: 2 </p>

      </div>

    </div>

    <p> 50 &dollar; </p>

  </div>

  <!-- Sub and total price -->
  <div class="totalprice">

    <p class="sub"> Subtotal <span> 50 &dollar; </span></p>

    <p class="del"> tax <span> 6.5 &dollar; </span> </p>

    <hr>

    <p class="tot"> Total <span> 56.5 &dollar; </span> </p>

  </div>

  <!-- Footer -->
  <footer> Move Recs Est 2023</footer>

</div>
  </body>



</template>

<script>
export default {
props: ['seatInfo'],
// Other component code
}
</script>

<style>
/* Our Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap');

/* Global */
* {
margin: 0;
padding: 0;
box-sizing: border-box;
font-family: 'Poppins'
}

body {
height: 100vh;
background-color: #D3E1E1
}

/* The Receipt */
.receipt {
width: 360px;
height: auto;
background-color: white;
border-radius: 30px;
position: absolute;
top: 70%;
left: 50%;
transform: translate(-50%, -50%);
box-shadow: 14px 14px 22px -18px;
padding: 20px;
}

/* Heading */
.name {
text-transform: uppercase;
text-align: center;
color: #6c8b8e;
letter-spacing: 10px;
font-size: 1.8em;
margin-top: 10px
}

/* Big thank */
.greeting {
font-size: 21px;
text-transform: capitalize;
text-align: center;
color: #6f8d90;
margin: 35px 0;
letter-spacing: 1.2px
}

/* Order info */
.order p {
font-size: 13px;
color: #aaa;
padding-left: 10px;
letter-spacing: .7px
}

/* Our line */
hr {
border: .7px solid #ddd;
margin: 15px 0;
}

/* Order details */
.details {
padding-left: 10px;
margin-bottom: 35px;
overflow: hidden
}

.details h3 {
font-weight: 400;
color: #6c8b8e;
font-size: 1.5em;
margin-bottom: 15px
}

/* Image and the info of the order */
.product {
float: left;
width: 83%
}

.product img {
width: 75px;
float: left
}

.product .info {
float: left;
margin-left: 15px
}

.product .info h4 {
color: #6f8d90;
font-weight: 400;
text-transform: uppercase;
margin-top: 10px
}

.product .info p {
font-size: 12px;
color: #aaa;
}

/* Net price */
.details > p {
color: #6f8d90;
margin-top: 25px;
font-size: 15px
}

/* Total price */
.totalprice p {
padding-left: 10px
}

.totalprice .sub,
.totalprice .del {
font-size: 13px;
color: #aaa
}

.totalprice span {
float: right;
margin-right: 17px
}

.totalprice .tot {
color: #6f8d90;
font-size: 15px
}

/* Footer */
footer {
font-size: 10px;
text-align: center;
margin-top: 20px; /* You can make it with position try it */
color: #aaa
}
</style>