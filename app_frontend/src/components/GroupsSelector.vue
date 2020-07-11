<template>
  <div class="row justify-content-center">
    <h1 class="text-center">Grupos para las materias de casos especiales</h1>

    <template v-for="studentClasses in classes">
      <div
        class="col-lg-12 text-center"
        v-for="studentClass in studentClasses"
        :key="studentClass.initials"
        v-if="studentClass.type && studentClass.type === 'special_case'"
      >
        <div class="form-group">
          <label :for="studentClass.initials">
            Grupo para <span>{{studentClass.name}} - {{studentClass.initials}}</span>
          </label>
          <input
            v-model="studentClass.group"
            type="text"
            class="form-control"
            :id="studentClass.initials"
            name="name"
            placeholder="p. ej. SA"
            @input="onInputGroup(studentClass, $event.target.value.toUpperCase())"
          />
        </div>
      </div>
    </template>

    <template v-if="showToastError">
      <toast-message
        :id="'groups-selection-error'"
        :content="'Tienes que ingresar los grupos para tus materias de caso especial'"
        @clickCloseToast="showToastError = false"
      ></toast-message>
    </template>

    <app-button @click="cancelGroupsSelection">
      <i class="fas fa-arrow-left"></i>
      Atr&aacute;s
    </app-button>
    <app-button @click="onConfirmGroupsSelection" class="ml-2">
      Siguiente
      <i class="fas fa-arrow-right"></i>
    </app-button>
  </div>
</template>

<script>
  import {mapActions, mapGetters} from "vuex";

  export default {
    data() {
      return {
        showToastError: false
      }
    },
    computed: mapGetters('groups', ['classes']),
    methods: {
      ...mapActions('groups', ['confirmGroupsSelection', 'cancelGroupsSelection', 'updateClassGroup']),
      onConfirmGroupsSelection: function () {
        const semesters = Object.entries(this.classes)
          .filter(semester => semester[1].find(klass => klass.type && klass.type === 'special_case') !== undefined);

        if (semesters === undefined) {
          this.showGroupsSelectionError();
          return;
        }

        let isInvalidGroupSelection = false;
        for (const semester of semesters) {
          const classes = semester[1];
          const invalidClass = classes.find(klass => klass.type && klass.type === 'special_case' && !klass.group);

          if (invalidClass) {
            isInvalidGroupSelection = true;
            break;
          }
        }
        if (isInvalidGroupSelection) {
          this.showGroupsSelectionError();
          return;
        }

        this.confirmGroupsSelection();
      },
      showGroupsSelectionError() {
        this.showToastError = true;
        setTimeout(() => $("#groups-selection-error").toast("show"), 0);
      },
      onInputGroup: function (classData, group) {
        this.updateClassGroup({classData, group})
      }
    }
  }
</script>

<style scoped>
  input {
    max-width: 100px;
    margin: auto;
  }

  label > span {
    font-weight: bold;
    font-size: 15px;
  }
</style>
