<template>
  <block-ab title="">
    <EntitiesImgScreen
      :instance="visiblePrinciple"
      :images="imagesPrinciple"
      :separatePage="true" />
  </block-ab>
</template>

<script>
export default {
  data() {
    return {
      visiblePrinciple: true,
      imagesPrinciple: [
        '/img/sliders/principle1.webp',
        '/img/sliders/principle2.webp',
        '/img/sliders/principle3.webp',
        '/img/sliders/principle4.webp',
        '/img/sliders/principle5.webp',
        '/img/sliders/principle6.webp',
        '/img/sliders/principle7.webp',
        '/img/sliders/principle8.webp',
        '/img/sliders/principle9.webp',
        '/img/sliders/principle10.webp',
        '/img/sliders/principle11.webp',
        '/img/sliders/principle12.webp',
      ],
    }
  },
}
</script>

<style scoped lang="scss"></style>
