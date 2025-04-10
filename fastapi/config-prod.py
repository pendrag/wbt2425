config_azure = { 
    # Database configuration
    'SQLALCHEMY_DATABASE_URL': "mysql+pymysql://csfmovqvbf:VHN7goZ$RiP2uafl@wbt2425-0-amr-server.mysql.database.azure.com/wbt2425-0-amr-database",
    # CORS origins
    'CORS_ORIGINS': [
        "https://wbt2425-0-amr-aydfbbc2ftfzeset.spaincentral-01.azurewebsites.net",
        # Add other origins as needed
    ],
}

config = { 
    # Database configuration
    'SQLALCHEMY_DATABASE_URL': "postgresql+pg8000://webapp:aySoH3Exiq0Ive6ZpDRRAfA1yycaIhRd@dpg-cvlvsk7gi27c73agulm0-a/webapp_xt7i",
    # CORS origins
    'CORS_ORIGINS': [
        "https://wbt2425.onrender.com",
        # Add other origins as needed
    ],
}

