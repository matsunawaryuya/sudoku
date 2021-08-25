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
            'related-cell': relatedCell(lineIndex, numberIndex),
            selected:
              selectedCell.rowIndex == lineIndex &&
              selectedCell.columnIndex == numberIndex,
          }"
          @click="selectCell(lineIndex, numberIndex)"
        >
          {{ number == 0 ? "" : number }}
        </td>
      </tr>
    </table>
    <div class="seletable-numbers">
      <button
        v-for="(number, i) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 'C']"
        :key="i"
        @click="setNumber(number)"
      >
        {{ number }}
      </button>
    </div>
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
      selectedCell: {
        rowIndex: -1,
        columnIndex: -1,
      },
    };
  },
  computed: {
    relatedCell: function () {
      return function (lineIndex, numberIndex) {
        const isSelectedRow = lineIndex == this.selectedCell.rowIndex;
        const isSelectedColumn = numberIndex == this.selectedCell.columnIndex;
        const selectedCellBaseRow =
          Math.floor(this.selectedCell.rowIndex / 3) ==
          Math.floor(lineIndex / 3);
        const selectedCellBaseColumn =
          Math.floor(this.selectedCell.columnIndex / 3) ==
          Math.floor(numberIndex / 3);
        return (
          isSelectedRow ||
          isSelectedColumn ||
          (selectedCellBaseRow && selectedCellBaseColumn)
        );
      };
    },
  },
  methods: {
    selectCell(lineIndex, numberIndex) {
      this.selectedCell.rowIndex = lineIndex;
      this.selectedCell.columnIndex = numberIndex;
    },
    setNumber(selectedNumber) {
      this.$set(
        this.numbers[this.selectedCell.rowIndex],
        this.selectedCell.columnIndex,
        selectedNumber == "C" ? 0 : selectedNumber
      );
    },
  },
};
</script>

<style lang="scss">
#app {
  box-sizing: border-box;
  margin-top: 60px;
  display: flex;
  justify-content: center;
  .sudoku {
    margin-right: 20px;
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
    .related-cell {
      background: rgba(243, 242, 170, 0.5);
    }
    .selected {
      background: rgba(245, 241, 44, 0.5);
    }
  }
  .seletable-numbers {
    display: flex;
    flex-direction: column;
    button {
      width: 50px;
      height: 50px;
      font-size: 24px;
      margin-bottom: 10px;
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
