<template>
  <label class="input">
    <p class="input__label">{{ label }}</p>
    <input class="input__self" :type="type" v-model="currentValue" :placeholder="placeholder" />
  </label>
</template>

<script>
export default {
  name: 'CommonInput',
  model: {
    prop: 'value',
    event: 'input',
  },
  props: {
    label: {
      type: String,
    },
    type: {
      type: String,
      default: 'text',
    },
    value: {
      type: [String, Number],
    },
    placeholder: {
      type: String,
    },
  },
  data() {
    return {
      currentValue: '',
      currentError: null,
    }
  },
  watch: {
    value: {
      handler() {
        this.currentValue = (this.value ?? '') + ''
      },
      immediate: true,
    },
    currentValue() {
      this.$emit('input', this.currentValue)
    },
  },
}
</script>

<style scoped lang="scss">
.input {
  display: block;
  &__label {
    @include tg(12px, 500, 12px, 0.4px);
    color: rgb(136, 136, 136);
    margin-bottom: 4px;
    user-select: none;
  }
  &__self {
    padding: 12px;
    @include tg(14px, 500, 14px, 0.4px);
    transition: border-color $t;
    border: 1px solid #dddddd;
    width: 100%;
    &::placeholder {
      color: rgba(136, 136, 136, 0.6);
    }
    &:focus,
    &:hover {
      border-color: #afafaf;
    }
  }
}
</style>
