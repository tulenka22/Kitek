<template>
  <block-ab title="Документы">
    <common-documents-list json-path="documents/documents-links.json" />
    <common-documents-list json-path="documents/documents-survey.json" />
    <a class="ab__link" href="/organization/survey"
      ><b red
        >Результаты анкетирования обучающихся, педагогических работников и работодателей:</b
      ></a
    >
    <common-documents-list json-path="documents/documents-contract.json" />
    <common-documents-list json-path="documents/documents-local-act.json" />
    <common-documents-list json-path="documents/documents-order.json" />
    <common-documents-list json-path="documents/documents-statement.json" />
  </block-ab>
</template>
