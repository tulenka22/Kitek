<template>
  <block-ab title="Международное сотрудничество">
    <!-- <p class="ab__p">
      Заключенных и планируемых к заключению договоров с иностранными и (или) международными
      организациями по вопросам образования и науки у БПОУ "КИТЭК" нет. Международной аккредитации
      образовательных программ нет.
    </p> -->
    <div class="doc-container">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper>
      <a
        href="/data/organization/Договор УКмТК.pdf"
        target="_blank"
        class="doc-link"
        style="
          color: #000000;
          text-decoration: none;
          border-bottom: 1px solid transparent;
          transition: border-bottom 0.3s;
        "
        @mouseover="$event.target.style.borderBottom = '1px solid rgb(112, 112, 255)'"
        @mouseleave="$event.target.style.borderBottom = '1px solid transparent'">
        Договор о международном сотрудничестве в сфере образования
      </a>
    </div>
  </block-ab>
</template>

<script>
export default {}
</script>

<style scoped lang="scss"></style>
