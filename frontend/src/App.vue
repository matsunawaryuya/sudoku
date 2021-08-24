<template>
  <div id="app">
    <table class="sudoku">
      <tr
        v-for="(line, lineIndex) in numbers"
        :key="lineIndex"
        :class="{
          'border-bottom': lineIndex == 2 || lineIndex == 5,
        }"
      >
        <td
          v-for="(number, numberIndex) in line"
          :key="numberIndex"
          :class="{
            'border-right': numberIndex == 2 || numberIndex == 5,
          }"
        >
          {{ number == 0 ? "" : number }}
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      numbers: [
        [0, 0, 5, 3, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 7, 0, 0, 1, 0, 5, 0, 0],
        [4, 0, 0, 0, 0, 5, 3, 0, 0],
        [0, 1, 0, 0, 7, 0, 0, 0, 6],
        [0, 0, 3, 2, 0, 0, 0, 8, 0],
        [0, 6, 0, 5, 0, 0, 0, 0, 9],
        [0, 0, 4, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 9, 7, 0, 0],
      ],
    };
  },
};
</script>

<style lang="scss">
#app {
  box-sizing: border-box;
  margin-top: 60px;
  .sudoku {
    margin: 0 auto;
    border-collapse: collapse;
    border: 3px solid #ccc;
    td {
      border: 1px solid #ccc;
      height: 80px;
      width: 80px;
      text-align: center;
      vertical-align: middle;
      font-size: 55px;
      cursor: pointer;
    }
  }
}
.border-bottom {
  border-bottom: 3px solid #ccc;
}
.border-right {
  border-right: 3px solid #ccc !important;
}
</style>
