<template>
  <div id="app">
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <!-- Form for creates instances of students-->
        <input
          type="text"
          class="form-control col-3 mx-2"
          placeholder="Name"
          v-model="student.name"
        />
        <input
          type="text"
          class="form-control col-3 mx-2"
          placeholder="Course"
          v-model="student.course"
        />
        <input
          type="text"
          class="form-control col-3 mx-2"
          placeholder="Rating"
          v-model="student.rating"
        />
        <button class="btn btn-success">Submit</button>
      </div>
    </form>
    <!--
      table.table>thead>th{Name}+th{Course}+th{Rating}^tbody>tr>td*3 = html shortcuts for :
    -->
    <table class="table">
      <thead>
        <th>Name</th>
        <th>Course</th>
        <th>Rating</th>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id" @dblclick="$data.student = student">
          <td>{{ student.name }}</td>
          <td>{{ student.course }}</td>
          <td>{{ student.rating }}</td>
          <td>
            <button class="btn btn-outline-danger sm mx-1" @click="deleteStudent(student)">x</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      student: {},
      students: [],
    };
  },
  async created() {
    await this.getStudents();
  }, // end created

  methods: {
    submitForm() {
      if (this.student.id === undefined) {
        this.createStudent();
      } else {
        this.editStudent();
      }
    }, // end submitForm
    async getStudents() {
      var response = await fetch("http://127.0.0.1:8000/RestAPP/students/");
      this.students = await response.json();
    }, // end getStudents
    async createStudent() {
      await this.getStudents();
      await fetch("http://127.0.0.1:8000/RestAPP/students/", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.student),
      });
      await this.getStudents();
    }, // end createStudent
    async editStudent() {
      await this.getStudents();
      await fetch(
        `http://127.0.0.1:8000/RestAPP/students/${this.student.id}/`, // dont forget `` instead of "" or ''
        {
          method: "put",
          headers: {
            "Content-Type": "applications/json",
          },
          body: JSON.stringify(this.student),
        }
      );
      await this.getStudents();
      this.student = {};
    }, // end editStudent
    async deleteStudent(student) {
      await this.getStudents();
      // dont forget `` instead of "" or ''
      await fetch(`http://127.0.0.1:8000/RestAPP/students/${student.id}/`, {
        method: "delete",
        headers: {
          "Content-Type": "applications/json",
        },
        body: JSON.stringify(this.student),
      });
      await this.getStudents();
      this.student = {};
    }, // end deleteStudent
  }, // end methods
}; /* end export default */
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
