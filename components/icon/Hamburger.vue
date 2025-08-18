<template>
  <svg
    viewBox="0 0 32 26"
    xmlns="http://www.w3.org/2000/svg"
    class="hamb"
    :class="{ 'hamb-active': active }"
  >
    <rect class="line line-1" />
    <rect class="line line-2" />
    <rect class="line line-3" />
  </svg>
</template>

<script>
export default {
  name: 'IconHamburger',
  props: {
    active: false,
  },
}
</script>

<style lang="scss" scoped>
.hamb {
  &-active {
    .line {
      &-1 {
        x: 12px;
      }
      &-2 {
        x: 8px;
      }
      &-3 {
        x: 16px;
      }
    }
  }
}
.line {
  width: 32px;
  height: 2px;
  transition: $t x, $t y;
  &-2 {
    y: 12px;
    x: 0px;
  }
  &-3 {
    y: 24;
  }
}
</style>
