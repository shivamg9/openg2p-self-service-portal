{
    "name": "G2P Service Provider Portal",
    "category": "G2P",
    "version": "15.0.1.2.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": [
        "g2p_self_service_portal",
        "g2p_program_reimbursement",
    ],
    "data": [
        "data/g2p_service_provider_form_action_data.xml",
        "views/auth_oauth_provider.xml",
        "views/g2p_service_provider_aboutus.xml",
        "views/g2p_service_provider_base.xml",
        "views/g2p_service_provider_contactus.xml",
        "views/g2p_service_provider_form_template.xml",
        "views/g2p_service_provider_form_submitted.xml",
        "views/g2p_service_provider_login.xml",
        "views/g2p_service_provider_myprofile.xml",
        "views/g2p_service_provider_others.xml",
        "views/g2p_service_provider_reimbursement.xml",
        "views/program_view.xml",
    ],
    "assets": {
        "web.assets_backend": [],
        "web.assets_qweb": [],
        "web.assets_frontend": [],
        "web.assets_common": [],
        "website.assets_editor": [
            "g2p_service_provider_portal/static/src/js/reim_form_editor.js",
        ],
    },
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
