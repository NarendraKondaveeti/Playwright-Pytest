class DisappearingElementsLocators:
    """Locators for the Disappearing Elements page"""

    # All links on the page
    ALL_LINKS = 'a'

    # Specific links that may disappear
    HOME_LINK = 'a:has-text("Home")'
    ABOUT_LINK = 'a:has-text("About")'
    CONTACT_US_LINK = 'a:has-text("Contact Us")'
    PORTFOLIO_LINK = 'a:has-text("Portfolio")'
    GALLERY_LINK = 'a:has-text("Gallery")'

    # Page heading
    PAGE_HEADING = 'h2'


