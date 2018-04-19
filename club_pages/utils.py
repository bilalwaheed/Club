from club_pages.models import DynamicData, SocialLink


def get_base_data():
    footer1 = DynamicData.objects.filter(page_data=DynamicData.FOOTER_SECTION1).first()
    footer2 = DynamicData.objects.filter(page_data=DynamicData.FOOTER_SECTION2).first()
    social_links = SocialLink.objects.all()

    return {'footer1': footer1, 'footer2': footer2, 'social': social_links}
