class JobCreateWizard():
    """
    contains all the functionality needed to navigate the job create
    wizard.
     """

    def __init__(self):
        pass

    def navigate_to_wizard(self):
        """
        Navigate browser to create wizard.
        """
        s = ''
        url = s.join(config['baseUrl']
                     + 'SC51/SC_RepairJob/aspx/repairjob_create_wzd.aspx')
        driver.get(job_create_wizard.url)
        text = "Welcome the the Repair Job Creation Wizard."
        assert text in driver.page_source
        return

    def set_workshop_site(self):
        """
        Sets the workshop site in the create job wizard.
        """
        pass

    def set_serial_number(self):
        """
        Set the serial number in the create job wizard.
        """
        pass

    def set_product_code(self):
        """
        Set the product code in the create job wizard.
        """
        pass

    def set_job_type(self):
        pass

    def set_flow_code(self):
        pass

    def set_ro_number(self):
        pass

    def set_job_site_number(self):
        pass

    def set_ship_site_number(self):
        pass

    def set_area(self):
        pass

    def set_engineer(self):
        pass

    def set_problem_code(self):
        pass

    def navigate_modal(self):
        pass

    def set_problem(self):
        pass

    def load_next_page(self, complete=False):
        """Go to next page in create job wizard.

        :complete: As bool, switches between next and finish.
        """
        pass
