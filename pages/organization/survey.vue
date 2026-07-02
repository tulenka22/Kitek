<template>
  <block-ab title="Анкетирование обучающихся, педагогических работников и работодателей">
    <b>Результаты анкетирования 2025 учебный год:</b>


    <common-documents-list json-path="documents/survey-38.02.04.json" />
    <common-documents-list json-path="documents/survey-38.02.05.json" />

    <common-documents-list json-path="documents/survey-43.02.15.json" />
  </block-ab>
</template>

<script>
export default {}
</script>

<style scoped lang="scss">
.center {
  margin-top: 24px;
  max-width: 1000px;
  > * {
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
