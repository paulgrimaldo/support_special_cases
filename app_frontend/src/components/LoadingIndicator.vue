<template>
  <div class="row justify-content-center">
    <div class="col-lg-12 text-center">
      <img class="logo" src="../assets/support_logo.svg" width="48px" height="48px" alt="Support Ficct"/>
      <p v-html="message"></p>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      message: {
        type: String,
        required: false,
        default: "Cargando ..."
      }
    }
  }
</script>

<style scoped>
  .logo {
    animation: rotate 2s infinite;
  }

  @keyframes rotate {
    100% {
      transform: rotateZ(360deg);
    }
  }
</style>
