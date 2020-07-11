<template>
  <div class="row justify-content-center">
    <div class="col-lg-12 text-center">
      <h1 v-html="processSummary.title"></h1>
      <p v-html="processSummary.summary"></p>
      <button
        v-html="processSummary.actionTitle"
        v-if="processSummary.actionTitle != null"
        :class="btnClass"
        @click="resetApp">
      </button>
    </div>
  </div>
</template>

<script>
  import {mapActions, mapState} from "vuex";

  export default {
    computed: {
      btnClass: function () {
        return this.success ? 'btn btn-dark mt-5' : 'btn btn-danger mt-5';
      },
      ...mapState(['processSummary'])
    },
    methods: mapActions(['resetApp'])
  }
</script>

<style scoped>

</style>
