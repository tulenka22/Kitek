<template>
  <block-ab title="Сведения об образовательной организации">
    <nav>
      <nuxt-link to="/organization" class="menu__link"> Основные сведения </nuxt-link>
      <nuxt-link to="/organization/structure" class="menu__link">
        Структура и органы управления образовательной организацией
      </nuxt-link>
      <nuxt-link to="/organization/documents" class="menu__link"> Документы </nuxt-link>

      <nuxt-link to="/education" class="menu__link"> Образование </nuxt-link>
      <nuxt-link to="/education/standarts" class="menu__link">
        Образовательные стандарты и требования
      </nuxt-link>
      <nuxt-link to="/education/paid" class="menu__link">
        Платные образовательные услуги
      </nuxt-link>

      <nuxt-link to="/organization/envrironment" class="menu__link"> Доступная среда </nuxt-link>
      <nuxt-link to="/education/digital" class="menu__link">
        Цифровая образовательная среда
      </nuxt-link>
      <nuxt-link to="/organization/international" class="menu__link">
        Международное сотрудничество
      </nuxt-link>

      <nuxt-link to="/organization/teaching-staff" class="menu__link">
        Руководство. Педагогический состав (научно-педагогический состав)
      </nuxt-link>
      <nuxt-link to="/organization/material-income" class="menu__link">
        Стипендии и меры поддержки обучающихся
      </nuxt-link>
      <nuxt-link to="/organization/logistics-equipment" class="menu__link">
        Материально-техническое обеспечение и оснащенность образовательного процесса
      </nuxt-link>
      <nuxt-link to="/organization/food-conditions" class="menu__link">
        Организация питания в образовательной организации
      </nuxt-link>
      <nuxt-link to="/organization/survey" class="menu__link">
        Анкетирование обучающихся, педагогических работников и работодателей
      </nuxt-link>

      <nuxt-link to="/organization/educational" class="menu__link">
        Воспитательная-деятельность
      </nuxt-link>

      <nuxt-link to="/organization/innovation" class="menu__link">
        Инновационно-методическая деятельность
      </nuxt-link>

      <nuxt-link to="/organization/mentor" class="menu__link"> Наставничество </nuxt-link>

      <nuxt-link to="/organization/fin-eco-activities" class="menu__link">
        Финансово-хозяйственная деятельность
      </nuxt-link>

      <nuxt-link to="/organization/transfer" class="menu__link">
        Вакантные места для приема (перевода) обучающихся
      </nuxt-link>

      <nuxt-link to="/organization/dostijenia" class="menu__link"> «Наши Достижения» </nuxt-link>
      <nuxt-link to="/organization/faq" class="menu__link"> «Часто задаваемые вопросы»</nuxt-link>
    </nav>
  </block-ab>
</template>

<script>
export default {}
</script>

<style scoped lang="scss">
@import '~/assets/common';
</style>
