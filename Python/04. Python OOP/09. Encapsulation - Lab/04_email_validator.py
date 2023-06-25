from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails: List[str], domains: List[str]):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name) -> bool:
        # return len(name) >= self.min_length  # проверява дали условието е изпълнено, ако е връща True, ако не е връща False
        if len(name) >= self.min_length:
            return True
        return False

    def __is_mail_valid(self, mail) -> bool:
        # return mail in self.mails
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain) -> bool:
        # return domain in self.domains
        if domain in self.domains:
            return True
        return False

    def validate(self, email: str) -> bool:
        return all([
            self.__is_name_valid(email.split('@')[0]),                 # от petar@abv.bg взима petar
            self.__is_mail_valid(email.split('@')[1].split('.')[0]),   # от petar@abv.bg взима abv
            self.__is_domain_valid(email.split('@')[1].split('.')[1])  # от petar@abv.bg взима bg
        ])



mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
