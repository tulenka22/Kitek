<template>
  <main
    class="page"
    :class="{
      textBackCollorBlack: isActiveTextBackCollorBlack,
      textBackCollorBrown: isActiveTextBackCollorBrown,
      textBackCollorBlue: isActiveTextBackCollorBlue,
      textBackCollorYellow: isActiveTextBackCollorYellow,
      textSizeMedium: isActiveTextSizeMedium,
      textSizeHigh: isActiveTextSizeHigh,
      hideImages: isActiveHideImages,
      blackWhiteImages: isActiveBWImages,
    }">
    <BlockSlider />
    <section class="page__content">
      <EventsRwo />
      <!-- <BlockEvents /> -->
      <!-- <newsnew /> -->
      <BannerMain />
      <BlockNews />
      <BlockSpecialties />
      <BlockProjects />
      <BlockLinks />
      <BlockMap />
    </section>
  </main>
</template>

<script>
import BannerMain from '~/components/block/BannerMain.vue'
import EventsRwo from '~/components/block/EventsRwo.vue'
import newsnew from '~/components/block/newsnew.vue'

export default {
  components: {
    EventsRwo,
    BannerMain,
    newsnew,
  },
  data() {
    return {
      isActiveTextSizeMedium: false,
      isActiveTextSizeHigh: false,
      isActiveTextBackCollorBlack: false,
      isActiveTextBackCollorBrown: false,
      isActiveTextBackCollorBlue: false,
      isActiveTextBackCollorYellow: false,
      isActiveHideImages: false,
      isActiveBWImages: false,
    }
  },
  mounted() {
    if (localStorage.getItem('isActiveBWImages')) {
      this.isActiveBWImages = true
    }

    if (localStorage.getItem('isActiveHideImages')) {
      this.isActiveHideImages = true
    }

    if (localStorage.getItem('isActiveTextBackCollorBlack')) {
      this.isActiveTextBackCollorBlack = true
    }

    if (localStorage.getItem('isActiveTextBackCollorYellow')) {
      this.isActiveTextBackCollorYellow = true
    }

    if (localStorage.getItem('isActiveTextBackCollorBlue')) {
      this.isActiveTextBackCollorBlue = true
    }

    if (localStorage.getItem('isActiveTextBackCollorBrown')) {
      this.isActiveTextBackCollorBrown = true
    }

    if (localStorage.getItem('isActiveTextSizeMedium')) {
      this.isActiveTextSizeMedium = true
    }

    if (localStorage.getItem('isActiveTextSizeHigh')) {
      this.isActiveTextSizeHigh = true
    }
  },
  watch: {
    isActiveTextSizeMedium(Boolean) {
      localStorage.isActiveTextSizeMedium = Boolean
    },
    isActiveTextSizeHigh(Boolean) {
      localStorage.isActiveTextSizeHigh = Boolean
    },
    isActiveTextBackCollorBlack(Boolean) {
      localStorage.isActiveTextBackCollorBlack = Boolean
    },
    isActiveTextBackCollorBrown(Boolean) {
      localStorage.isActiveTextBackCollorBrown = Boolean
    },
    isActiveTextBackCollorBlue(Boolean) {
      localStorage.isActiveTextBackCollorBlue = Boolean
    },
    isActiveTextBackCollorYellow(Boolean) {
      localStorage.isActiveTextBackCollorYellow = Boolean
    },
    isActiveHideImages(Boolean) {
      localStorage.isActiveHideImages = Boolean
    },
    isActiveBWImages(Boolean) {
      localStorage.isActiveBWImages = Boolean
    },
  },
}
</script>

<style scoped lang="scss">
.page {
  overflow: hidden;
  &__content {
    padding: 70px;
    @include medium-media {
      padding: 24px 8px;
    }
  }
}
</style>
