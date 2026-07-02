<template>
  <Navdrop :columns="columns" />
</template>

<script>
import { createLink, createColumn } from '~/core/helpers/link'
export default {
  name: 'NavdropOrganization',
  data() {
    return {
      columns: [
        createColumn(
          '',
          createLink('/organization', 'Основные сведения'),
          createLink(
            '/organization/structure',
            'Структура и органы управления образовательной организацией'
          ),
          createLink('/organization/documents', 'Документы'),
          createLink('/education', 'Образование'),
          createLink('/education/standarts', 'Образовательные стандарты и требования'),
          createLink('/education/paid', 'Платные образовательные услуги'),
          createLink('/organization/envrironment', 'Доступная среда'),
          createLink('/education/digital', 'Цифровая образовательная среда'),
          createLink('/organization/international', 'Международное сотрудничество')
        ),
        createColumn(
          '',

          createLink('/organization/pedsostav', 'Руководство'),
          createLink(
            '/organization/teaching-staff',
            'Педагогический состав (научно-педагогический состав)'
          ),
          createLink('/organization/material-income', 'Стипендии и меры поддержки обучающихся'),
          createLink(
            '/organization/logistics-equipment',
            'Материально-техническое обеспечение и оснащенность образовательного процесса'
          ),
          createLink(
            '/organization/food-conditions',
            'Организация питания в образовательной организации'
          ),
          createLink(
            '/organization/survey',
            'Анкетирование обучающихся, педагогических работников и работодателей'
          )
        ),
        createColumn(
          '',
          createLink('/organization/educational', 'Воспитательная деятельность'),
          createLink('/organization/innovation', 'Инновационно-методическая деятельность '),
          createLink('/organization/mentor', 'Наставничество '),
          createLink('/organization/fin-eco-activities', 'Финансово-хозяйственная деятельность'),
          createLink('/organization/transfer', 'Вакантные места для приема (перевода) обучающихся'),
          createLink('/organization/dostijenia', '«Наши Достижения»'),
          createLink('/organization/faq', '«Часто задаваемые вопросы»')
        ),
      ],
    }
  },
}
</script>
