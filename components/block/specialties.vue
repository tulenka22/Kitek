<template>
  <div class="specialties">
    <div class="overlay" :class="{ 'overlay-active': overlayState }">
      <div class="overlay__wrapper" v-if="selectedSpec">
        <header class="overlay__header">
          <h1 class="overlay__h1">{{ selectedSpec.title }}</h1>
          <IconWrapper class="overlay__close" width="32" height="32" @click="overlayState = false">
            <IconClose />
          </IconWrapper>
        </header>
        <main class="overlay__content">
          <h2 class="overlay__h2">Специальности данной группы</h2>
          <div class="overlay__scroll">
            <EntitiesSpecialityCard
              v-for="(spec, idx) of selectedSpec.specialties"
              :key="idx"
              :instance="spec" />
          </div>
        </main>
      </div>
    </div>
    <AppBlock
      title="Укрупнённые группы специальностей и профессий"
      :without-body="true"
      :block-style="{ padding: '0' }" />
    <EntitiesSpeciality
      v-for="(spec, idx) of specialties"
      :key="idx"
      :instance="spec"
      @overlay-change-state="overlayChangeState" />
  </div>
</template>

<script>
import { specialties } from '~/core/lists'
export default {
  name: 'BlockSpecialties',
  data() {
    return {
      specialties,
      // Mobile
      overlayState: false,
      selectedSpec: null,
    }
  },
  methods: {
    overlayChangeState(state, id) {
      this.overlayState = state
      this.selectedSpec = this.specialties.find((spec) => spec.id === id)
    },
  },
}
</script>

<style lang="scss" scoped>
.specialties {
  margin-top: 60px;
  &::v-deep .el {
    margin-top: 24px;
    @include medium-media {
      margin-top: 12px;
    }
  }
}
.overlay {
  transition: $t opacity, $t left;
  position: fixed;
  bottom: 0;
  left: 100%;
  right: 0;
  top: 0;
  background-color: $bg-primary;
  height: 100vh;
  width: 100%;
  pointer-events: none;
  opacity: 0;
  z-index: 100000;
  &__header {
    display: flex;
    align-items: center;
    padding: 12px;
    border-bottom: 1px solid $border-color;
  }
  &__h1 {
    flex-grow: 1;
    @include tg(18px, 500, 22px, 2px, 'Montserrat');
  }
  &__h2 {
    color: $nav-link;
    @extend %tg-h2-mobile;
    padding: 12px 12px 0 12px;
  }
  &__wrapper {
    height: 100%;
  }
  &__content {
    height: 100%;
    overflow: hidden;
  }
  &__scroll {
    padding: 0 12px 0 12px;
    &::v-deep .card {
      margin-top: 16px;
    }
  }
  &__close {
    color: $primary-color;
  }
  &-active {
    left: 0;
    pointer-events: all;
    opacity: 1;
  }
}
</style>
