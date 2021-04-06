<template>
  <div class="hello">
    <h1>In English: {{ msg }}</h1>
    <h1>Displaing information for quesiton: {{ questionId }}</h1>

    <h3 v-if="loading">Loading data....</h3>
    <h3 v-else>{{ data }}</h3>

  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import TutorialDataService from '../nxbase_api';
import Todo from '../nxbase_api';

@Component
export default class HelloWorld extends Vue {
  @Prop() private msg!: string;
  @Prop() private questionId!: string;
  loading=true;
  data: typeof Todo [] = [];


  async mounted() {
    console.log("I am in mounted")
    this.data = await TutorialDataService.allQuestion("https://jsonplaceholder.typicode.com/todos/");
    //this.data = await http<Todo[]>("https://jsonplaceholder.typicode.com/todos");
    console.log(this.data[0].userId)
    const question = await TutorialDataService.question("https://jsonplaceholder.typicode.com/todos/", 1);
    console.log(question);
    this.loading=false;



  }


}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
