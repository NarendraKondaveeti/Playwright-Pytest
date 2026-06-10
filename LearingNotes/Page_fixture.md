`@pytest.fixture(scope="function")

`def page(browser):

    context = browser.new_context()

    page = context.new_page()

    yield page

    context.close()

**`@pytest.fixture(scope="function")`**

Ee line dvara `page()` function ni Pytest fixture ga register chestunnam. `scope="function"` ani ivvadam valla prati test function execute ayye mundu ee fixture okkasari run avutundi. Ante oka test ki oka fresh page create avutundi. Oka test lo jarigina changes vere test meeda effect chupinchakunda isolation maintain cheyyadaniki function scope use chestaru. Ee line lekapothe `page()` anedi normal Python function matrame avutundi, fixture laga Pytest handle cheyyadu.

**`def page(browser):`**

Ikkada `page` ane fixture create chestunnam. `browser` ane parameter ni chusthe, ee fixture ki browser dependency undi ani ardham. Browser value ni manam manually pass cheyyadam ledu. Pytest already unna `browser` fixture ni execute chesi, dani return value ni ikkada inject chestundi. Ante mundu browser ready ayyaka matrame page fixture execute avutundi.

**`context = browser.new_context()`**

Ikkada browser lo kotta browser context create chestunnam. Context ni simple ga cheppali ante browser lo separate user session laanti di. Prati context ki own cookies, local storage, session storage untayi. Oka context lo login ayina information vere context ki share avvadu. Testing lo isolation maintain cheyyadaniki context use chestaru. Browser open cheyyadam veru, browser context create cheyyadam veru.

**`page = context.new_page()`**

Ikkada context lopala actual browser tab create avutundi. Playwright lo manam direct ga browser meeda actions perform cheyyam. Page object meeda actions perform chestam. Click, fill, navigate, locator, assertions laanti operations anni page object dvara jarugutayi. Kabatti ee line tarvata manaki actual automation cheyyadaniki ready ga unna page object vastundi.

**`yield page`**

Ikkadi varaku setup phase complete ayindi. Browser context create ayindi, page create ayindi. Ippudu aa page object ni test case ki provide chestunnam. `yield` use cheyyadam valla fixture temporary ga pause avutundi mariyu page object test ki available avutundi. Test execution complete ayyaka control malli yield kinda unna code daggaraki vastundi.

**`context.close()`**

Test complete ayyaka browser context ni close chestunnam. Context close avvadam valla aa context lo create ayina pages, cookies, sessions, storage data anni clean-up avutayi. Oka test data vere test ki leak avvakunda proper clean-up jarugutundi. Browser motham close cheyyadam ledu, kevalam ee test kosam create chesina context ni matrame close chestunnam. Anduke function scope fixture lo context create chesi, test complete ayyaka context close cheyyadam common practice.

Mothamga ee fixture purpose enti ante: browser fixture nundi browser ni teesukoni, prati test kosam oka fresh browser context mariyu page create chesi, aa page ni test ki provide chesi, test complete ayyaka context ni clean-up cheyyadam.
