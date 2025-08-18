<template>
  <div class="spec-el" :class="{ 'spec-el-active': state }">
    <header class="spec-el__header">
      <h2>{{ specTitle() }}</h2>
      <IconWrapper
        width="48"
        height="48"
        class="spec-el__close"
        @click="updateState(false)"
      >
        <IconCircleClose />
      </IconWrapper>
    </header>

    <div class="spec-el__content">
      <EntitiesSpecialityCard
        v-for="(spec, idx) of specialties"
        :key="idx"
        :instance="spec"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'EntitiesSpecialityList',
  props: {
    state: {
      type: Boolean,
    },
    specialties: {
      type: Array,
    },
    instance: {
      type: Object,
    },
  },
  methods: {
    updateState(state) {
      this.$emit('state:update', state)
    },
    specTitle() {
      if (this.instance.id === 4 || this.instance.id === 1)
        return 'Профессии и специальности данной группы'
      return 'Специальности данной группы'
    },
  },
}
</script>

<style lang="scss" scoped>
.spec-el {
  position: absolute;
  transition: ease 0.6s top, $t opacity;
  top: 100%;
  left: 0;
  height: calc(100% - 102px);
  width: 100%;
  z-index: 50;
  background-color: $bg-primary;
  border-radius: 0 0 5px 5px;
  box-shadow: $special-shadow;
  opacity: 0;
  &__content {
    padding: 12px 48px 64px 48px;
    max-height: 456px;
    overflow-y: auto;
    @include scrollbar;
    &::v-deep .card {
      margin-top: 16px;
    }
  }
  &__close {
    color: $accent-color;
    cursor: pointer;
  }
  &__header {
    padding: 24px 48px 24px 48px;
    @extend %tg-h3;
    display: flex;
    align-items: center;
    border-bottom: 1px solid $border-color;
    > h2 {
      margin-top: 4px;
      flex-grow: 1;
    }
  }
  &-active {
    top: 102px;
    opacity: 1;
  }
}
</style>
