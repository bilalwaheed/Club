from club_pages.models import DynamicData, SocialLink, Sponser


def get_base_data():
    footer1 = DynamicData.objects.filter(page_data=DynamicData.FOOTER_SECTION1).first()
    footer2 = DynamicData.objects.filter(page_data=DynamicData.FOOTER_SECTION2).first()
    footer3 = DynamicData.objects.filter(page_data=DynamicData.FOOTER_SECTION3).first()
    email = DynamicData.objects.filter(page_data=DynamicData.EMAIL).first()
    phone = DynamicData.objects.filter(page_data=DynamicData.PHONE).first()
    social_links = SocialLink.objects.all()
    sponsers = Sponser.objects.all().order_by('-id')[:4]

    return {'footer1': footer1, 'footer2': footer2, 'footer3': footer3, 'email': email, 'phone': phone,
            'social': social_links, 'sponsers': sponsers}
