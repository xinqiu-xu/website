from pathlib import Path
from string import Template

root = Path(r"E:\wert")

shared_head = """<meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <link rel=\"stylesheet\" href=\"${prefix}assets/css/shared.css\">\n  <link rel=\"stylesheet\" href=\"${prefix}assets/css/${variant}.css\">\n  <script src=\"${prefix}assets/js/site-data.js\" defer></script>\n  <script src=\"${prefix}assets/js/site.js\" defer></script>"""


def wrap(title_key, page_key, variant, prefix, body, footer_link):
    shell = f"""<!DOCTYPE html>
<html lang=\"zh-CN\">
<head>
  {shared_head}
  <title></title>
</head>
<body data-title-key=\"{title_key}\" data-page=\"{page_key}\" class=\"{variant}\">
  <header class=\"site-header\">
    <div class=\"header-inner\">
      <div class=\"brand-block\">
        <span class=\"brand-eyebrow\">MCU PROJECT 61</span>
        <h1 class=\"brand-title\" data-i18n=\"titleIndex\">智能垃圾分类机器人</h1>
      </div>
      <nav class=\"site-nav\">
        <ul>
          <li><a data-nav=\"home\" href=\"{prefix}{variant}/\" data-i18n=\"home\">首页</a></li>
          <li><a data-nav=\"cases\" href=\"{prefix}{variant}/cases/\" data-i18n=\"navCases\">应用场景</a></li>
          <li><a data-nav=\"about\" href=\"{prefix}{variant}/about/\" data-i18n=\"navAbout\">关于我们</a></li>
          <li><a data-nav=\"gallery\" href=\"{prefix}{variant}/gallery/\" data-i18n=\"navGallery\">图像展示</a></li>
        </ul>
      </nav>
      <div class=\"header-actions\">
        <button class=\"lang-button\" type=\"button\" data-toggle-lang>中文/EN</button>
      </div>
    </div>
  </header>
  <main>
    <div class=\"site-shell\">
{body}
    </div>
  </main>
  <footer class=\"site-footer\">
    <div class=\"footer-inner\">
      <p>© 2026 微控项目61组</p>
      <a href=\"{footer_link}\" class=\"button secondary\" data-i18n=\"allVersions\">All Versions</a>
    </div>
  </footer>
</body>
</html>"""
    return Template(shell).substitute(prefix=prefix, variant=variant)


home_heroes = {
    "v1": """      <section class=\"hero\">\n        <div class=\"hero-copy\">\n          <p class=\"brand-eyebrow\" data-i18n=\"variantTheme\">设计主题</p>\n          <h2 data-i18n=\"slogan1\">引领智慧环保新变革</h2>\n          <p data-i18n=\"slogan2\">智能分拣的微光，点亮绿色未来的每一步</p>\n          <div class=\"hero-actions\">\n            <a class=\"button primary\" href=\"./product/\" data-i18n=\"learnMore\">了解更多</a>\n            <a class=\"button secondary\" href=\"./gallery/\" data-i18n=\"galleryTitle\">图像展示</a>\n          </div>\n        </div>\n        <div class=\"hero-visual\"><img src=\"../assets/media/img1.jpg\" alt=\"device\"></div>\n      </section>""",
    "v2": """      <section class=\"hero\">\n        <div class=\"hero-copy\">\n          <p class=\"brand-eyebrow\">Project Defense</p>\n          <h2 data-i18n=\"slogan1\">引领智慧环保新变革</h2>\n          <p data-i18n=\"introLine1\">一款面向校园、社区、公共空间的轻量化智能垃圾分类装置</p>\n          <div class=\"hero-actions\">\n            <a class=\"button primary\" href=\"./product/\" data-i18n=\"learnMore\">了解更多</a>\n            <a class=\"button secondary\" href=\"./cases/\" data-i18n=\"titleScene\">应用场景与成果</a>\n          </div>\n        </div>\n        <div class=\"hero-visual\"><video src=\"../assets/media/video1.mp4\" muted loop autoplay playsinline></video></div>\n      </section>""",
    "v3": """      <section class=\"hero\">\n        <div class=\"hero-copy\">\n          <p class=\"brand-eyebrow\">Eco Living</p>\n          <h2 data-i18n=\"slogan1\">引领智慧环保新变革</h2>\n          <p data-i18n=\"slogan2\">智能分拣的微光，点亮绿色未来的每一步</p>\n          <div class=\"hero-actions\">\n            <a class=\"button primary\" href=\"./product/\" data-i18n=\"learnMore\">了解更多</a>\n          </div>\n        </div>\n        <div class=\"hero-visual\"><img src=\"../assets/media/img1.jpg\" alt=\"device\"></div>\n      </section>""",
    "v4": """      <section class=\"hero\">\n        <div class=\"hero-copy\">\n          <p class=\"brand-eyebrow\">Control Dashboard</p>\n          <h2 data-i18n=\"titleIndex\">智能垃圾分类机器人</h2>\n          <p data-i18n=\"introLine2\">以嵌入式技术为核心，实现稳定、高效、低成本的环境辅助管理</p>\n          <div class=\"hero-actions\">\n            <a class=\"button primary\" href=\"./product/\" data-i18n=\"learnMore\">了解更多</a>\n          </div>\n        </div>\n        <div class=\"hero-visual\"><video src=\"../assets/media/video1.mp4\" muted loop autoplay playsinline></video></div>\n      </section>""",
    "v5": """      <section class=\"hero\">\n        <div class=\"hero-copy\">\n          <p class=\"brand-eyebrow\">Exhibition Poster</p>\n          <h2 data-i18n=\"slogan1\">引领智慧环保新变革</h2>\n          <p data-i18n=\"quote\">科技向善，用智能与责任共建绿色低碳新生活</p>\n          <div class=\"hero-actions\">\n            <a class=\"button primary\" href=\"./product/\" data-i18n=\"learnMore\">了解更多</a>\n            <a class=\"button secondary\" href=\"./about/\" data-i18n=\"titleAbout\">关于我们</a>\n          </div>\n        </div>\n        <div class=\"hero-visual\"><img src=\"../assets/media/img1.jpg\" alt=\"device\"></div>\n      </section>""",
    "v6": """      <section class=\"hero\">\n        <div class=\"hero-copy\">\n          <p class=\"brand-eyebrow\">Minimal Story</p>\n          <h2 data-i18n=\"titleIndex\">智能垃圾分类机器人</h2>\n          <p data-i18n=\"introLine1\">一款面向校园、社区、公共空间的轻量化智能垃圾分类装置</p>\n          <div class=\"hero-actions\">\n            <a class=\"button primary\" href=\"./product/\" data-i18n=\"learnMore\">了解更多</a>\n          </div>\n        </div>\n        <div class=\"hero-visual\"><img src=\"../assets/media/img1.jpg\" alt=\"device\"></div>\n      </section>""",
}

home_tail = """      <div class=\"grid-two\">\n        <section class=\"section-card\">\n          <h3 data-i18n=\"projectIntro\">项目简介</h3>\n          <p data-i18n=\"introLine1\">一款面向校园、社区、公共空间的轻量化智能垃圾分类装置</p>\n          <p style=\"margin-top:12px; color: var(--muted);\" data-i18n=\"introLine2\">以嵌入式技术为核心，实现稳定、高效、低成本的环境辅助管理</p>\n        </section>\n        <section class=\"section-card\">\n          <h3 data-i18n=\"structure\">产品结构</h3>\n          <ul class=\"feature-list\">\n            <li data-i18n=\"module1\">距离探测模块</li>\n            <li data-i18n=\"module2\">满溢检测模块</li>\n            <li data-i18n=\"module3\">语音交互模块</li>\n            <li data-i18n=\"module4\">中央控制系统</li>\n          </ul>\n        </section>\n      </div>\n\n      <section class=\"quote-panel\">\n        <strong data-i18n=\"quoteLead\">绿色智能</strong>\n        <blockquote data-i18n=\"quote\">科技向善，用智能与责任共建绿色低碳新生活</blockquote>\n      </section>\n\n      <div class=\"metrics-grid\">\n        <article class=\"metric-card\">\n          <span class=\"metric-value\">40%</span>\n          <p class=\"metric-label\" data-i18n=\"effUp\">清运效率提升：40%</p>\n        </article>\n        <article class=\"metric-card\">\n          <span class=\"metric-value\">60%</span>\n          <p class=\"metric-label\" data-i18n=\"costDown\">人力成本下降：60%</p>\n        </article>\n        <article class=\"metric-card\">\n          <span class=\"metric-value\">95%+</span>\n          <p class=\"metric-label\" data-i18n=\"accuracy\">分类准确率：95%+</p>\n        </article>\n      </div>"""

product_body = """      <section class=\"page-banner\">\n        <h2 data-i18n=\"titleProduct\">产品详情</h2>\n        <p data-i18n=\"appearanceDesc\">一体化机身设计，占地面积小，适配室内外各类场景，仓体标识清晰，投放更方便。</p>\n      </section>\n\n      <div class=\"grid-two\">\n        <section class=\"section-card\">\n          <h3 data-i18n=\"appearance\">产品外观</h3>\n          <p data-i18n=\"appearanceDesc\">一体化机身设计，占地面积小，适配室内外各类场景，仓体标识清晰，投放更方便。</p>\n          <div class=\"hero-actions\" style=\"margin-top:18px;\">\n            <a class=\"button primary\" href=\"../more/\" data-i18n=\"structure\">产品结构</a>\n            <a class=\"button secondary\" href=\"../gallery/\" data-i18n=\"galleryTitle\">图像展示</a>\n          </div>\n        </section>\n        <section class=\"media-preview\"><img src=\"../../assets/media/img1.jpg\" alt=\"device\"></section>\n      </div>\n\n      <section class=\"section-heading\">\n        <div>\n          <h2 data-i18n=\"structure\">产品结构</h2>\n          <p data-i18n=\"introLine2\">以嵌入式技术为核心，实现稳定、高效、低成本的环境辅助管理</p>\n        </div>\n      </section>\n      <div class=\"modules-grid\">\n        <article class=\"module-card\"><h3 data-i18n=\"module1\">距离探测模块</h3></article>\n        <article class=\"module-card\"><h3 data-i18n=\"module2\">满溢检测模块</h3></article>\n        <article class=\"module-card\"><h3 data-i18n=\"module3\">语音交互模块</h3></article>\n        <article class=\"module-card\"><h3 data-i18n=\"module4\">中央控制系统</h3></article>\n      </div>"""

more_body = """      <section class=\"page-banner\">\n        <h2 data-i18n=\"titleModule\">产品结构 - 模块详情</h2>\n        <p data-i18n=\"introLine2\">以嵌入式技术为核心，实现稳定、高效、低成本的环境辅助管理</p>\n      </section>\n\n      <div class=\"modules-grid\">\n        <article class=\"module-card\"><h3 data-i18n=\"module1\">距离探测模块</h3><p data-i18n=\"desc1\">采用高精度测距传感器，实时检测投放口距离，实现智能感应与安全防护。</p></article>\n        <article class=\"module-card\"><h3 data-i18n=\"module2\">满溢检测模块</h3><p data-i18n=\"desc2\">实时监测容器容量，达到阈值自动触发满溢提醒。</p></article>\n        <article class=\"module-card\"><h3 data-i18n=\"module3\">语音交互模块</h3><p data-i18n=\"desc3\">支持语音提示与指令交互，操作简单，提升使用体验。</p></article>\n        <article class=\"module-card\"><h3 data-i18n=\"module4\">中央控制系统</h3><p data-i18n=\"desc4\">以高性能芯片为核心，统一调度各模块，保障系统稳定运行。</p></article>\n      </div>\n\n      <div class=\"hero-actions\" style=\"margin-top:28px;\">\n        <a class=\"button secondary\" href=\"../product/\" data-i18n=\"backProduct\">返回产品介绍</a>\n      </div>"""

cases_body = """      <section class=\"page-banner\">\n        <h2 data-i18n=\"titleScene\">应用场景与成果</h2>\n        <p data-i18n=\"galleryHint\">支持查看图片与演示视频，展示设备外观与运行效果。</p>\n      </section>\n\n      <div class=\"grid-two\">\n        <section class=\"section-card\">\n          <h3 data-i18n=\"scene\">适用场景</h3>\n          <ul class=\"page-list\">\n            <li data-i18n=\"resiArea\">居民小区</li>\n            <li data-i18n=\"schoolArea\">校园</li>\n            <li data-i18n=\"officeArea\">写字楼</li>\n            <li data-i18n=\"mallArea\">商场</li>\n          </ul>\n        </section>\n        <section class=\"section-card\">\n          <h3 data-i18n=\"effect\">项目效果</h3>\n          <ul class=\"feature-list\">\n            <li data-i18n=\"effUp\">清运效率提升：40%</li>\n            <li data-i18n=\"costDown\">人力成本下降：60%</li>\n            <li data-i18n=\"accuracy\">分类准确率：95%+</li>\n          </ul>\n        </section>\n      </div>"""

about_body = """      <section class=\"page-banner\">\n        <h2 data-i18n=\"titleAbout\">关于我们</h2>\n        <p data-i18n=\"teamDesc\">我们是微控项目61组，致力于用自动化与嵌入式技术解决环保问题。</p>\n      </section>\n\n      <div class=\"grid-two\">\n        <section class=\"section-card\">\n          <h3 data-i18n=\"team\">团队介绍</h3>\n          <p data-i18n=\"teamDesc\">我们是微控项目61组，致力于用自动化与嵌入式技术解决环保问题。</p>\n        </section>\n        <section class=\"section-card\">\n          <h3 data-i18n=\"contact\">联系我们</h3>\n          <ul class=\"page-list\">\n            <li data-i18n=\"emailText\">邮箱：team@example.com</li>\n            <li data-i18n=\"schoolText\">学校：西安电子科技大学</li>\n          </ul>\n        </section>\n      </div>"""

gallery_body = """      <section class=\"page-banner\">\n        <h2 data-i18n=\"galleryTitle\">图像展示</h2>\n        <p data-i18n=\"galleryHint\">支持查看图片与演示视频，展示设备外观与运行效果。</p>\n      </section>\n\n      <div class=\"gallery-grid\">\n        <article class=\"media-card\">\n          <div class=\"media-preview\"><img src=\"../../assets/media/img1.jpg\" alt=\"device image\"></div>\n          <h3 data-i18n=\"picText\">图片</h3>\n          <p data-i18n=\"imageCaption\">设备外观展示</p>\n          <button type=\"button\" data-open-media=\"image\" data-i18n=\"picText\">图片</button>\n        </article>\n        <article class=\"media-card\">\n          <div class=\"media-preview\"><video src=\"../../assets/media/video1.mp4\" muted playsinline preload=\"metadata\"></video></div>\n          <h3 data-i18n=\"videoText\">视频</h3>\n          <p data-i18n=\"videoCaption\">设备演示视频</p>\n          <button type=\"button\" data-open-media=\"video\" data-i18n=\"videoText\">视频</button>\n        </article>\n      </div>\n\n      <div class=\"modal\" data-modal>\n        <div class=\"modal-dialog\">\n          <button class=\"modal-close\" type=\"button\" data-modal-close aria-label=\"Close\">×</button>\n          <img src=\"../../assets/media/img1.jpg\" alt=\"device image\" hidden>\n          <video src=\"../../assets/media/video1.mp4\" controls playsinline hidden></video>\n        </div>\n      </div>"""

for variant in ["v1", "v2", "v3", "v4", "v5", "v6"]:
    (root / variant / "index.html").write_text(
        wrap("titleIndex", "home", variant, "../", home_heroes[variant] + "\n\n" + home_tail, "../index.html"),
        encoding="utf-8",
    )
    (root / variant / "product" / "index.html").write_text(
        wrap("titleProduct", "product", variant, "../../", product_body, "../../index.html"),
        encoding="utf-8",
    )
    (root / variant / "more" / "index.html").write_text(
        wrap("titleModule", "more", variant, "../../", more_body, "../../index.html"),
        encoding="utf-8",
    )
    (root / variant / "cases" / "index.html").write_text(
        wrap("titleScene", "cases", variant, "../../", cases_body, "../../index.html"),
        encoding="utf-8",
    )
    (root / variant / "about" / "index.html").write_text(
        wrap("titleAbout", "about", variant, "../../", about_body, "../../index.html"),
        encoding="utf-8",
    )
    (root / variant / "gallery" / "index.html").write_text(
        wrap("galleryTitle", "gallery", variant, "../../", gallery_body, "../../index.html"),
        encoding="utf-8",
    )

entry = """<!DOCTYPE html>
<html lang=\"zh-CN\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <link rel=\"stylesheet\" href=\"./assets/css/shared.css\">
  <script src=\"./assets/js/site-data.js\" defer></script>
  <script src=\"./assets/js/site.js\" defer></script>
  <title></title>
</head>
<body data-title-key=\"variantEntryTitle\">
  <header class=\"site-header\">
    <div class=\"header-inner\">
      <div class=\"brand-block\">
        <span class=\"brand-eyebrow\">MCU PROJECT 61</span>
        <h1 class=\"brand-title\" data-i18n=\"variantEntryTitle\">微控制器宣传网页设计方案</h1>
      </div>
      <div class=\"header-actions\">
        <button class=\"lang-button\" type=\"button\" data-toggle-lang>中文/EN</button>
      </div>
    </div>
  </header>
  <main>
    <div class=\"site-shell\">
      <section class=\"hero\">
        <div class=\"hero-copy\">
          <p class=\"brand-eyebrow\">Design Collection</p>
          <h2 data-i18n=\"variantEntryTitle\">微控制器宣传网页设计方案</h2>
          <p data-i18n=\"variantEntryDesc\">以下 6 套网页保持同一内容与中英文切换能力，但在视觉风格、首页布局与展示方式上各不相同。</p>
        </div>
        <div class=\"hero-visual\"><img src=\"./assets/media/img1.jpg\" alt=\"device\"></div>
      </section>
      <section class=\"section-heading\">
        <div>
          <h2 data-i18n=\"variantTheme\">设计主题</h2>
          <p data-i18n=\"variantEntryDesc\">以下 6 套网页保持同一内容与中英文切换能力，但在视觉风格、首页布局与展示方式上各不相同。</p>
        </div>
      </section>
      <div class=\"variant-grid\" data-variant-list></div>
    </div>
  </main>
  <footer class=\"site-footer\">
    <div class=\"footer-inner\">
      <p>© 2026 微控项目61组</p>
      <p>6 variants / 36 pages / bilingual</p>
    </div>
  </footer>
</body>
</html>"""
(root / "index.html").write_text(entry, encoding="utf-8")
print("site generated")
