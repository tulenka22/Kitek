<template>
  <button class="btn" :class="`btn-${variant}`" v-on="listener">
    <slot />
  </button>
</template>

<script>
export default {
  name: 'CommonButton',
  props: {
    variant: {
      type: String,
      default: 'red',
    },
  },
  computed: {
    listener() {
      return Object.assign({}, this.$listeners, {
        click: (e) => this.$emit('click', e),
      })
    },
  },
}
</script>

<style scoped lang="scss">
.btn {
  transition: $t background-color;
  border-radius: 8px;
  @extend %tg-h3;
  padding: 12px 48px;
  &-red {
    background-color: $primary-color;
    color: $bg-control;
    &:hover {
      background-color: saturate($primary-color, $amount: 10);
    }
  }
}
</style>
