report_names = [
    "Convegenius Education Dashboard",
    "bank exceutives",
    "Bihar Vikas Mission",
    "Crime_Report",
    "CRM",
    "E-Commerce Dashboard",
    "Health_ICCC_Dashboard",
    "HR Analytics_Dashboard",
    "Insurance Incentive Dashboard",
    "PMO Dashboard",
    "Scheme Management Dashboard",
    "Taxi Trip Report",
    "Water Quality",
    "Sales_Analysis",
    "Safety Dashboard",
    "Water resource",
    "Hospital management",
    "Grievance Management",
    "Public transport dashboard",
    "India Energy",
    "School Education",
    "Real estate",
    "Primary school dashboard",
    "Scheme Management 1",
    "Pharmaceutical Analysis",
]

report_ids = [
    "7cab0a58-4039-49f8-848b-9c067f452bd9",
    "0e99c3e4-a339-453c-89bd-31cf07197152",
    "E7c1f7b5-545c-423e-8002-353223cccb6d",
    "b61b2fb8-9bed-45af-bd74-a8d5d1fd5230",
    "bc9b29db-86c0-4b8c-a8aa-cf4fc6daa59f",
    "b127fe7c-342c-4ef4-be41-30c1c6221489",
    "5c9468d9-82c0-42c4-844e-71138943e755",
    "1a59db89-a04e-45fb-a360-b70992b98a40",
    "71530e68-a1e3-4bc9-84dc-66b19fac0230",
    "c039ff48-6ec9-4a40-a2b5-f68fdb67dc4d",
    "eaa2ba26-3a0b-4b80-979f-8d1d5d63dbc4",
    "a3e9d51a-aea6-4baa-ae25-b8a167f86c45",
    "779b8943-bcd9-41e6-aa53-3294ebe0f529",
    "bc2247a4-1eb9-4bce-80d8-c61232dca32a",
    "65779adb-97ee-4dbc-bf61-3cfea4b44ec6",
    "12805e2e-b423-4c98-b4ed-6570cd893483",
    "cab2e932-67e8-42c1-add7-51de14a30515",
    "e8c9eab8-d070-41c3-8000-bc960b22940e",
    "f4aff47b-f340-435d-84bb-65878af8bca2",
    "44319f3a-c6c1-41a4-a018-45281d704a86",
    "aadaad7b-d859-496f-96e5-9654b272fad2",
    "4091a4fe-e578-4a9b-a953-447601a416a8",
    "7fdc3f2f-ae84-4d3d-809b-3cc4caa35451",
    "f4735a2c-72d8-4e6b-aca5-12efb5105834",
    "8eae3a90-ad55-4b8b-8bec-806ff685efef",
]
for name, r_id in zip(report_names, report_ids):
    Report.objects.create(
        name=name,
        report_id=r_id,
    )
