<template>
  <block-ab title="Приёмная комиссия">
    <div class="block-zxc__right">
      <common-documents-list json-path="documents/committee-links.json" />
    </div>
    <div class="logos">
      <a class="ab__link" href="https://omsktec.ru/professional"
        ><img
          alt="Logo Профессионалитет"
          target="_blank"
          src="/img/professional/ЛогоПроф2024.png"
          class="logoProf"
      /></a>
      <div>
        <img
          alt="Logo СтройПодряд"
          target="_blank"
          src="/img/professional/companies/4.png"
          class="logoStroypodryad" />
        <p class="ab__p" style="text-align: center">Опорная организация</p>
      </div>
    </div>
    <video class="ab__video" controls>
      <source src="/video/rolik.mp4" type="video/mp4" />
      Ваш браузер не поддерживает видео
    </video>
    <video class="ab__video" controls>
      <source src="/video/rolik1.mp4" type="video/mp4" />
      Ваш браузер не поддерживает видео
    </video>
    <p class="ab__p">
      <b
        >Бюджетное профессиональное образовательное учреждение Омской области «Колледж инновационных
        технологий, экономики и коммерции»</b
      >
      является открытым инновационным образовательным учреждением с развивающейся
      культурно-образовательной средой, обеспечивающей качество подготовки компетентного
      специалиста, воспитание творческой социально-успешной личности гражданина и патриота.
    </p>
    <div class="center">
      <h2 class="ab__subtitle">
        <b red-prim></b>
      </h2>
    </div>
    <ul class="ab__list">
      <ul class="ul__square">
        <li>
          <p class="ab__p">
            <b>Режим работы приемной комиссии:</b>
          </p>
        </li>
      </ul>

      <p class="ab__p">
        <b>с 02.06.2025 по 30.06.2025 </b>
      </p>
      <li>Пн-Пт: 09:00-16:00</li>
      <li>Сб-Вс: Выходной</li>
      <p class="ab__p">
        <b>с 01.07.2025 по 15.08.2025 </b>
      </p>
      <li>Пн-Чт: 09:00-17:00</li>
      <li>Пт: 09:00-16:00</li>
      <li>Сб: 10:00-14:00</li>
      <li>Вс: Выходной</li>
    </ul>
    <p class="ab__p">
      Кулик Маргарита Владимировна, ответственный секретарь приемной комиссии: ---
    </p>

    <ul class="ul__square">
      <li>
        <p class="ab__p">
          <b>Прием документов осуществляется по адресу:</b>
        </p>
      </li>
    </ul>
    <p class="ab__p">
      <a
        href="https://2gis.ru/omsk/firm/282003257722518?m=73.38383%2C55.026562%2F16"
        target="_blank"
        ><b>Адрес 2 GIS</b>: г. Омск, ул. 27-я Северная, 69.</a
      >
    </p>
    <p class="ab__p"><b>Телефон</b>: 8 (3812) 68-07-66</p>

    <!-- <ul class="ab__list spec-li">
      <p class="ab__p"><b red>Специальности/профессии</b></p>
      <li v-for="spec of specialties" :key="spec.id">
        <nuxt-link
          v-if="
            spec.name != '40.02.01 ПРАВО И ОРГАНИЗАЦИЯ СОЦИАЛЬНОГО ОБЕСПЕЧЕНИЯ' &&
            spec.name != '43.02.14 ГОСТИНИЧНОЕ ДЕЛО'
          "
          class="ab__link"
          :to="`/specialties/${spec.code}`">
          {{ spec.name }}
        </nuxt-link>
      </li>
    </ul> -->
    <ul class="ab__list spec-li">
      <p class="ab__p">
        <b red
          >Специальности/профессии реализуемые в рамках федерального проекта «Профессионалитет»:</b
        >
      </p>
      <li v-if="fpSpecialties.length">
        <ul>
          <li v-for="spec of fpSpecialties" :key="spec.id">
            <nuxt-link
              v-if="
                spec.name != '40.02.01 ПРАВО И ОРГАНИЗАЦИЯ СОЦИАЛЬНОГО ОБЕСПЕЧЕНИЯ' &&
                spec.name != '43.02.14 ГОСТИНИЧНОЕ ДЕЛО'
              "
              class="ab__link"
              :to="`/specialties/${spec.code}`">
              {{ spec.name }}
            </nuxt-link>
          </li>
        </ul>
      </li>
      <p class="ab__p">
        <b red>Специальности/профессии:</b>
      </p>
      <li v-if="otherSpecialties.length">
        <ul>
          <li v-for="spec of otherSpecialties" :key="spec.id">
            <nuxt-link
              v-if="
                spec.name != '40.02.01 ПРАВО И ОРГАНИЗАЦИЯ СОЦИАЛЬНОГО ОБЕСПЕЧЕНИЯ' &&
                spec.name != '43.02.14 ГОСТИНИЧНОЕ ДЕЛО'
              "
              class="ab__link"
              :to="`/specialties/${spec.code}`">
              {{ spec.name }}
            </nuxt-link>
          </li>
        </ul>
      </li>
    </ul>
    <a style="height: 10px; width: 10px; left: 0px; position: absolute; background: white"></a>
    <ul class="ab__list">
      <ul class="ul__square">
        <li>
          <p class="ab__p">
            <b>Перечень документов, предоставляемых в приемную комиссию колледжa: <b red> * </b></b>
          </p>
        </li>
      </ul>

      <li>документ, удостоверяющий личность, гражданство (копия);</li>
      <li>документ об образовании и (или) документ об образовании (квалификации) (копия);</li>
      <li>4 фотографии 3*4 см (заочное отделение 2 шт).</li>
    </ul>
    <p class="ab__p small__text">
      <b red> * </b> Поступающие вправе направить заявление о приеме и все необходимые документы
      через операторов почтовой связи общего пользования, а также воспользоваться функционалом
      федеральной государственной информационной системы «Единый портал государственных и
      муниципальных услуг» или региональных порталов государственных и муниципальных услуг.
    </p>
    <p class="ab__p small__text">
      <b red> ** </b> Возможность подачи поступающим документов в электронной форме в соответствии с
      ФЗ «Об электронной подписи» от 06.04.2011 № 63-ФЗ, ФЗ «Об информации, информационных
      технологиях и о защите информации» от 27.07.2006 № 149-ФЗ, ФЗ «О связи» от 07.07.2003 № 126-ФЗ
      в Колледже предусмотрена, при наличии у абитуриента электронной цифровой подписи.
    </p>
    <ul class="ab__list">
      <ul class="ul__square">
        <li>
          <p class="ab__p">
            <b>
              Перечень документов, предоставляемых в приемную комиссию колледжa в электронном виде
              по всем специальностям/профессиям направляется по электронной почте:
              omsktec2020@mail.ru, телефон 8(3812)68-07-66 <b red> * </b>
            </b>
          </p>
        </li>
      </ul>
    </ul>
    <p class="ab__p small__text">
      <b red> * </b>Документы, необходимые для поступления, предоставляются (направляются) в
      организацию в электронной форме (документ на бумажном носителе, преобразованный в электронную
      форму путем сканирования или фотографирования с обеспечением машиночитаемого распознавания его
      реквизитов).
    </p>

    <ul class="ab__list">
      <p class="ab__p">
        <b red>Требующиеся документы:</b>
      </p>
      <li>
        <a class="ab__link" target="_blank" href="/data/enrolle/Шаблон заявления 2025.pdf"
          >Заявление (с личной подписью абитуриента)<b red> * </b>
          <icon-wrapper class="ab__icon" width="12" height="16"><icon-document /></icon-wrapper
        ></a>
      </li>
      <p class="ab__p">
        В соответствии с изменениями в нормативно-правовых актах, регламентирующих прием
        абитуриентов, в заявлении поступающим
        <b> указывается страховой номер индивидуального лицевого счета (СНИЛС)!</b><b red> * </b>
      </p>
      <li>Документ, удостоверяющий личность, гражданство (копия)</li>
      <li>
        Документ об образовании и (или) документ об образовании (квалификации) (копия): титульный
        лист и приложение
      </li>
      <li>4 фотографии 3*4 см (заочное отделение: 2 шт)</li>
      <li>
        <a
          >Согласие на обработку персональных данных (с личной подписью абитуриента или законного
          представителя)
        </a>
        <ul>
          <li>
            <a
              class="ab__link"
              target="_blank"
              href="/data/enrolle/Согласие на обработку персональных данных для несовершеннолетних.pdf">
              - для несовершеннолетних<icon-wrapper class="ab__icon" width="12" height="16"
                ><icon-document /></icon-wrapper
            ></a>
          </li>
          <li>
            <a
              class="ab__link"
              target="_blank"
              href="/data/enrolle/Согласие на обработку персональных данных для совершеннолетних.pdf">
              - для совершеннолетних<icon-wrapper class="ab__icon" width="12" height="16"
                ><icon-document /></icon-wrapper
            ></a>
          </li>
        </ul>
      </li>
      <li>
        Медицинская справка установленного образца Ф-086у, подтверждающая отсутствие
        противопоказаний по состоянию здоровья для поступления на выбранную специальность/профессию.
      </li>
      <li>
        <a
          class="ab__link"
          target="_blank"
          href="/data/enrolle/Лист ознакомления с перечнем мед.противовпоказаний.pdf">
          Лист ознакомления с перечнем медицинских противопоказании (с личной подписью абитуриента
          или законного представителя)
          <b red> ** </b
          ><icon-wrapper class="ab__icon" width="12" height="16"><icon-document /></icon-wrapper
        ></a>
      </li>
      <p class="ab__p small__text">
        <b red> * </b>
        <a
          href="/data/enrolle/о внесении изменений в порядок приема на обучение по образовательным программам СПО.pdf"
          target="_blank">
          <b>Приказ Министерства просвещения РФ №915 от 20.10.2022 г.</b> «О внесении изменений в
          порядок приёма на обучение по образовательным программам среднего профессионального
          образования, утвержденный приказом Министерства просвещения РФ №457 от 02.09.2020 г.».
        </a>
      </p>
      <p class="ab__p small__text">
        <b red> ** </b> Для абитуриентов поступающих на специальности:
      </p>
      <ul class="ab__p small__text">
        <li>26.02.05 Эксплуатация судовых энергетических установок</li>
        <li>26.01.09 Моторист судовой</li>
        <li>43.02.15 Поварское и кондитерское дело</li>
        <li>43.01.09 Повар, кондитер</li>
      </ul>
    </ul>
    <p v-if="!plan">{{ error }}</p>
    <div v-else class="table-center">
      <br />
      <h2 class="ab__subtitle" @click="table_plan = !table_plan">
        <b red-prim>Количество поданных документов</b>
      </h2>
      <p class="ab__p small__text">
        по состоянию на {{ plan.data }}, (Кликните на табличку для отображения информации)
      </p>
      <table class="a-table">
        <thead @click="table_plan = !table_plan">
          <tr class="a-table__header click">
            <th class="a-table__cell a-table__cell-center" rowspan="3">Специальность</th>
            <th class="a-table__cell a-table__cell-center" colspan="4">Очное отделение (бюджет)</th>
            <th class="a-table__cell a-table__cell-center" colspan="2">
              Заочное отделение (бюджет)
            </th>
          </tr>
          <tr class="a-table__header click">
            <th class="a-table__cell a-table__cell-center" colspan="2">9 класс</th>
            <th class="a-table__cell a-table__cell-center" colspan="2">11 класс</th>
            <th class="a-table__cell a-table__cell-center" colspan="2">11 класс</th>
          </tr>
          <tr class="a-table__header click">
            <th class="a-table__cell a-table__cell-center">План</th>
            <th class="a-table__cell a-table__cell-center">Подано заявлений</th>
            <th class="a-table__cell a-table__cell-center">План</th>
            <th class="a-table__cell a-table__cell-center">Подано заявлений</th>
            <th class="a-table__cell a-table__cell-center">План</th>
            <th class="a-table__cell a-table__cell-center">Подано заявлений</th>
          </tr>
        </thead>
        <tbody v-show="table_plan">
          <tr v-for="stat in plan.p" :key="stat.spec">
            <td class="a-table__cell a-table__cell-8">
              {{ stat.spec }}
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">
              {{ stat.p9 }}
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">
              {{ stat.s9 }}
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">
              {{ stat.p11 }}
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">
              {{ stat.s11 }}
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">
              {{ stat.z_p11 }}
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">
              {{ stat.z_s11 }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="center">
      <h2 class="ab__subtitle">
        <b red-prim>Уважаемые абитуриенты, колледж общежития не имеет!</b>
      </h2>
    </div>
    <p class="ab__p">
      <b red> Вступительные испытания </b>
      <br />
      Прием в колледж по всем образовательным программам, формам обучения проводится без
      вступительных испытаний. Обучение ведется на русском языке. Колледж оказывает содействие в
      трудоустройстве. Выпускники колледжа работают в лучших организациях Омской области.
    </p>
    <p class="ab__p">
      <b red> Доступная среда </b>
      <br />
      В соответствии с требованиями ФЗ «Об образовании в Российской Федерации» п.10,11 статья 79
      колледжем для получения образования обучающимся с ограниченными возможностями здоровья созданы
      специальные условия:
    </p>
    <ul class="ab__p ul__dash small__text">
      <li>на прилегающей территории размещен пандус;</li>
      <li>приобретен мобильный гусеничный подъемник;</li>
      <li>выделены контрастным цветом дверные проемы;</li>
      <li>кромки ступеней оклеены светящийся в темноте лентой;</li>
      <li>установлены указатели направления, тактильные таблички;</li>
      <li>оборудовано санитарно-гигиеническое помещение;</li>
      <li>
        предоставляются бесплатно специальные учебники и учебные пособия, иная учебная литература
        (за счет средств субъекта Российской Федерации);
      </li>
      <li>
        предоставляются бесплатно услуги сурдопереводчиков и тифлосурдопереводчиков (за счет средств
        субъекта Российской Федерации);
      </li>
      <li>
        предоставлена возможность использования персонального компьютера, специальной беспроводной
        полнофункциональной компьютерной клавиатурой с большими разноцветными клавишами вместе с
        программным обеспечением SuperNova Magnifer and Speech.
      </li>
    </ul>
    <p class="ab__p">
      В Министерстве образования Омской области работает "Горячая линия" по вопросам приема в
      профессиональные образовательные организации инвалидов и лиц с ограниченными возможностями
      здоровья на период в режиме телефонной связи +7 (3812) 24-75-39 Лунёва Татьяна Владимировна
    </p>
    <div class="table-center">
      <p class="ab__p" style="cursor: pointer" v-on:click="table = !table">
        <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
        ><b red-prim>Проходной балл 2025</b>
      </p>
      <table class="a-table">
        <thead v-on:click="table = !table">
          <tr class="a-table__header click">
            <th class="a-table__cell a-table__cell-head">Специальности/профессии</th>
            <th class="a-table__cell a-table__cell-head">Уровень образования</th>
            <th class="a-table__cell a-table__cell-head">Проходной балл</th>
          </tr>
        </thead>
        <tbody v-show="table">
          <tr>
            <td class="a-table__cell a-table__cell-8">
              09.02.07 Информационные системы и программирование (программист)
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">4,15</td>
          </tr>
          <tr>
            <td class="a-table__cell a-table__cell-8">
              09.02.07 Информационные системы и программирование (разработчик веб и мультимедийных
              приложений)
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">4,01</td>
          </tr>
          <tr>
            <td class="a-table__cell a-table__cell-8" rowspan="2">
              38.02.01 Экономика и бухгалтерский учет (по отраслям)
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">4,05</td>
          </tr>
          <tr>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">11 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">3,53</td>
          </tr>
          <tr>
            <td class="a-table__cell a-table__cell-8" rowspan="2">
              38.02.08 Торговое дело (направленность: Коммерция)
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">4,01</td>
          </tr>
          <tr>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">11 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">3,32</td>
          </tr>
          <tr></tr>
          <tr>
            <td class="a-table__cell a-table__cell-8" rowspan="2">
              38.02.08 Торговое дело (направленность: Товароведение)
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">3,69</td>
          </tr>
          <tr>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">11 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">3,46</td>
          </tr>
          <!-- <tr>
            <td class="a-table__cell a-table__cell-8">
              40.02.01 Право и организация социального обеспечения
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">3,93</td>
          </tr>
        -->
          <tr>
            <td class="a-table__cell a-table__cell-8">43.01.09 Повар, кондитер</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">3,53</td>
          </tr>

          <tr>
            <td class="a-table__cell a-table__cell-8" rowspan="2">
              43.02.15 Поварское и кондитерское дело
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">3,79</td>
          </tr>
          <tr>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">11 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">3,50</td>
          </tr>

          <tr>
            <td class="a-table__cell a-table__cell-8">
              43.02.16 Туризм и гостеприимство (направленность: Гостиничные услуги)
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">4,11</td>
          </tr>
          <tr>
            <td class="a-table__cell a-table__cell-8">
              43.02.16 Туризм и гостеприимство (направленность: Экскурсионные услуги)
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">4,06</td>
          </tr>

          <tr>
            <td class="a-table__cell a-table__cell-8">26.01.09 Моторист судовой</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">3,06</td>
          </tr>
          <tr>
            <td class="a-table__cell a-table__cell-8">
              26.02.05 Эксплуатация судовых энергетических установок
            </td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">9 классов</td>
            <td class="a-table__cell a-table__cell-8 a-table__cell-center">3,11</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p @click="advantage = !advantage" class="ab__p click ab__link">
      <b red-prim>Преимущество колледжа - сотрудничество с ВУЗами</b>
    </p>
    <h2 class="ab__subtitle" @click="table_plan = !table_plan">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><a href="\data\programa-d-s\Рубрика-Вопрос-ответ.pdf"
        ><b red-prim>Наиболее часто задаваемые вопросы о поступлении в колледж</b></a
      >
    </h2>
    <p class="ab__p click ab__link">
      <b red-prim
        ><icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
        ><a href="https://vk.com/im?media=&sel=-63457955">Вопросы и ответы</a></b
      >
    </p>
    <div v-show="advantage">
      <p class="ab__p"><b>Омский государственный технический университет</b></p>
      <p class="ab__p">
        Факультет «Экономика, сервис и управление», кафедра «Экономика предприятий и организаций»,
        направление «Экономика»
      </p>
      <p class="ab__p">
        Факультет «Художественно-технологический» , кафедра «Биотехнологичная технология
        общественного питания и товароведение» направления:
      </p>
      <p class="ab__p">«Товароведение и экспертиза потребительских товаров»</p>
      <p class="ab__p">«Технология продуктов общественного питания»</p>
      <p class="ab__p"><b>Сибирский юридический университет</b>, направление</p>
      <p class="ab__p">
        «Юристпруденция», профили: «Налогово-правовой», «Государственно – правовой» «Гражданско –
        правовой»
      </p>
      <p class="ab__p">
        <b>Финансовый университет при Правительстве РФ</b>, факультет «Экономика» направления:
      </p>
      <p class="ab__p">«Финансы и кредит»,</p>
      <p class="ab__p">«Учет, анализ, аудит».</p>
    </div>
    <h2 class="ab__subtitle"><b red>Наши социальные сети</b></h2>
    <div class="contacts__row">
      <div class="contacts__row contacts__socials">
        <a href="https://vk.com/omsktec" target="_blank" class="icon contacts__social">
          <IconWrapper width="24" height="24">
            <IconVK />
          </IconWrapper>
        </a>
        <a href="https://ok.ru/group/53402328629468" target="_blank" class="icon contacts__social">
          <IconWrapper width="24" height="24">
            <IconOK />
          </IconWrapper>
        </a>
        <!-- <a href="https://t.me/omskkitec" target="_blank" class="icon contacts__social">
          <IconWrapper width="24" height="24">
            <IconTelegram />
          </IconWrapper>
        </a> -->
      </div>
    </div>
    <swiper class="slider_committe" :options="swiperOptions">
      <swiper-slide>
        <h2 class="ab__subtitle"><b red>Библиотека</b></h2>
        <img class="img-single__minimg" alt="Slider-Image" src="/img/committee/Библиотека.jpg" />
      </swiper-slide>
      <swiper-slide>
        <h2 class="ab__subtitle"><b red>IT-лаборатория</b></h2>
        <img
          class="img-single__minimg"
          alt="Slider-Image"
          src="/img/committee/Компьютерный класс.jpg" />
      </swiper-slide>
      <swiper-slide>
        <h2 class="ab__subtitle"><b red>Спортивный зал</b></h2>
        <img
          class="img-single__minimg"
          alt="Slider-Image"
          src="/img/committee/Спортивный зал.jpg" />
      </swiper-slide>
      <swiper-slide>
        <h2 class="ab__subtitle"><b red>Мастерская по компетенции "Поварское дело"</b></h2>
        <img class="img-single__minimg" alt="Slider-Image" src="/img/committee/Мастерские.jpg" />
      </swiper-slide>
      <swiper-slide>
        <h2 class="ab__subtitle"><b red>Столовая</b></h2>
        <img class="img-single__minimg" alt="Slider-Image" src="/img/committee/Столовая.jpg" />
      </swiper-slide>
    </swiper>

    <common-documents-list class="document-list" json-path="documents/committee-links.json" />
  </block-ab>
</template>

<!-- <script>
import Block from '~/components/app/Block.vue'
import { loadDynamic } from '~/core/helpers/file'
export default {
  components: { Block },
  data() {
    return {
      plan: null,
      swiperOptions: {
        grabCursor: true,
        autoplay: {
          enabled: true,
          delay: 5000,
        },
      },
      title: 'Приёмная комиссия',
      description:
        'Бюджетное профессиональное образовательное учреждение Омской области «Колледж инновационных технологий, экономики и коммерции». Колледж ведет подготовку по следующим Специальностям/профессиям, 09.02.07 ИНФОРМАЦИОННЫЕ СИСТЕМЫ И ПРОГРАММИРОВАНИЕ (КВАЛИФИКАЦИЯ – ПРОГРАММИСТ), 09.02.07 ИНФОРМАЦИОННЫЕ СИСТЕМЫ И ПРОГРАММИРОВАНИЕ (КВАЛИФИКАЦИЯ – РАЗРАБОТЧИК WEB И МУЛЬТИМЕДИЙНЫХ ПРИЛОЖЕНИЙ), 40.02.04 ЮРИСПРУДЕНЦИЯ, 38.02.01 ЭКОНОМИКА И БУХГАЛТЕРСКИЙ УЧЕТ (ПО ОТРАСЛЯМ), 38.02.04 КОММЕРЦИЯ (ПО ОТРАСЛЯМ), 43.02.16 ТУРИЗМ И ГОСТЕПРИИМСТВО, 38.02.05 ТОВАРОВЕДЕНИЕ И ЭКСПЕРТИЗА КАЧЕСТВА ПОТРЕБИТЕЛЬСКИХ ТОВАРОВ, 43.02.15 ПОВАРСКОЕ И КОНДИТЕРСКОЕ ДЕЛО, 43.01.09 ПОВАР, КОНДИТЕР, 26.01.09 МОТОРИСТ СУДОВОЙ, 26.02.05 ЭКСПЛУАТАЦИЯ СУДОВЫХ ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК',
      jsonPath: 'dynamic/rating/plan.json',
      table_plan: false,
      table: false,
      advantage: false,
    }
  },
  head() {
    return {
      title: this.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.description,
        },
      ],
    }
  },
  async created() {
    try {
      this.plan = JSON.parse(await loadDynamic(this.jsonPath))
    } catch {
      this.error = `Ошибка при загрузке документа '${this.jsonPath}'`
    }
  },
  methods: {},
  computed: {
    specialties() {
      return this.$store.state.specialties
    },
  },
}
</script> -->
<script>
import Block from '~/components/app/Block.vue'
import { loadDynamic } from '~/core/helpers/file'
export default {
  components: { Block },
  data() {
    return {
      plan: null,
      swiperOptions: {
        grabCursor: true,
        autoplay: {
          enabled: true,
          delay: 5000,
        },
      },
      title: 'Приёмная комиссия',
      description:
        'Бюджетное профессиональное образовательное учреждение Омской области «Колледж инновационных технологий, экономики и коммерции». Колледж ведет подготовку по следующим Специальностям/профессиям, 09.02.07 ИНФОРМАЦИОННЫЕ СИСТЕМЫ И ПРОГРАММИРОВАНИЕ (КВАЛИФИКАЦИЯ – ПРОГРАММИСТ), 09.02.07 ИНФОРМАЦИОННЫЕ СИСТЕМЫ И ПРОГРАММИРОВАНИЕ (КВАЛИФИКАЦИЯ – РАЗРАБОТЧИК WEB И МУЛЬТИМЕДИЙНЫХ ПРИЛОЖЕНИЙ), 40.02.04 ЮРИСПРУДЕНЦИЯ, 38.02.01 ЭКОНОМИКА И БУХГАЛТЕРСКИЙ УЧЕТ (ПО ОТРАСЛЯМ), 38.02.04 КОММЕРЦИЯ (ПО ОТРАСЛЯМ), 43.02.16 ТУРИЗМ И ГОСТЕПРИИМСТВО, 38.02.05 ТОВАРОВЕДЕНИЕ И ЭКСПЕРТИЗА КАЧЕСТВА ПОТРЕБИТЕЛЬСКИХ ТОВАРОВ, 43.02.15 ПОВАРСКОЕ И КОНДИТЕРСКОЕ ДЕЛО, 43.01.09 ПОВАР, КОНДИТЕР, 26.01.09 МОТОРИСТ СУДОВОЙ, 26.02.05 ЭКСПЛУАТАЦИЯ СУДОВЫХ ЭНЕРГЕТИЧЕСКИХ УСТАНОВОК',
      jsonPath: 'dynamic/rating/plan.json',
      table_plan: false,
      table: false,
      advantage: false,
    }
  },
  head() {
    return {
      title: this.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.description,
        },
      ],
    }
  },
  async created() {
    try {
      this.plan = JSON.parse(await loadDynamic(this.jsonPath))
    } catch {
      this.error = `Ошибка при загрузке документа '${this.jsonPath}'`
    }
  },
  methods: {},
  computed: {
    specialties() {
      return this.$store.state.specialties
    },
    fpSpecialties() {
      const fpSpecialties = []
      const otherSpecialties = []

      this.specialties.forEach((specialtie) => {
        if (specialtie.group === 'ФП') {
          fpSpecialties.push(specialtie)
        } else {
          otherSpecialties.push(specialtie)
        }
      })

      return fpSpecialties
    },
    otherSpecialties() {
      const fpSpecialties = []
      const otherSpecialties = []

      this.specialties.forEach((specialtie) => {
        if (specialtie.group === 'ФП') {
          fpSpecialties.push(specialtie)
        } else {
          otherSpecialties.push(specialtie)
        }
      })

      return otherSpecialties
    },
  },
}
</script>

<style scoped>
.ab__video {
  width: 100%;
  margin: 0 auto;
  max-width: 800px; /* Максимальная ширина видео */
  padding: 20px; /* Отступы вокруг видео */
  background-color: #f0f0f0; /* Фоновый цвет */
  border-radius: 10px; /* Закругленные углы */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Тень */
}

.ab__video video {
  width: 100%; /* Ширина видео */
  height: auto; /* Автоматическая высота */
  border-radius: 10px; /* Закругленные углы */
}

/* Медиа-запросы для адаптивности */

@media (max-width: 768px) {
  .ab__video {
    padding: 10px; /* Уменьшение отступов на меньших экранах */
  }
}

@media (max-width: 480px) {
  .ab__video {
    padding: 5px; /* Ещё меньше отступов на очень маленьких экранах */
  }
}
.ab__table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}

.ab__table th,
.ab__table td {
  border: 1px solid #ccc;
  padding: 5px;
}

.ab__table th {
  text-align: center;
}

.ab__table td {
  vertical-align: top;
}

.ab__table tr:nth-child(even) {
  background-color: #f2f2f2;
}
</style>

<style lang="scss" scoped>
//Сейчас здесь будет конфетти!
.ab {
  &__icon {
    color: $primary-color;
    display: inline;
  }
  &__overflow {
    max-width: 100vw;
    overflow: auto;
  }
}
.ul {
  &__dash {
    > li {
      list-style-type: none;
      &::before {
        content: '-';
        margin-right: 6px;
      }
    }
  }
  &__square {
    position: relative;
    > li {
      margin-top: 8px;
      list-style-type: none;
      &::before {
        content: '▀';
        top: 4px;
        left: -15px;
        position: absolute;
        margin-right: 6px;
        color: $primary-color;
      }
    }
  }
}
.small {
  &__text {
    @extend %tg-event-card-subtitle;
    @include medium-media() {
      font-size: 14px;
    }
  }
}
b[red-prim] {
  color: $primary-color;
}
.table {
  max-width: 1000px;
  &-center {
    overflow: auto;
  }
}
.center {
  margin-top: 24px;
  max-width: 1000px;
  > * {
    margin-left: auto;
    margin-right: auto;
  }
}
.slider_committe {
  margin: 0px;
  margin-top: 24px;
  max-width: 1000px;
}
.click {
  cursor: pointer;
}
.contacts {
  flex: none;
  &__row {
    display: flex;
  }
  &__social {
    &:nth-child(even) {
      margin: 0 12px;
    }
  }
  &__socials {
    flex-grow: 1;
  }
}

.logos {
  display: flex;
}

.logoProf,
.logoStroypodryad {
  width: auto;
}

@media screen and (max-width: 768px) {
  .logoProf {
    width: 100%;
  }

  .logoStroypodryad {
    width: 100%;
    height: auto;
    padding-top: 0;
    margin-top: 20px;
  }
}

@media screen and (min-width: 400px) and (max-width: 766px) {
  .logoProf {
    width: 230px;
    height: auto;
  }
  .logoStroypodryad {
    width: 270px;
    height: auto;
    margin-top: 15px;
  }
}

@media screen and (min-width: 768px) {
  .logoProf {
    width: 300px;
    height: auto;
  }
  .logoStroypodryad {
    width: 300px;
    height: 180px;
    margin-top: 30px;
  }
}

@media screen and (max-width: 556px) {
  // .logos {
  //   flex-direction: column;
  // }
  .logoProf,
  .logoStroypodryad {
    width: 50%;
  }
}
</style>
