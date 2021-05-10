        
try:
            # Check if 'min' has any strings. If it does, then print an error.
            # When the second 'for loop' is done checking 'min', the first loop then changes 
            # from 'min' to 'max' for the second 'for loop' to check.
            num_list = [min, max]
            valid_num = "[0-9]"

            if num_list[0] == "":
                self.error_label.config(text="Min is blank, please enter a valid number.")
                return
            elif num_list[1] == "":
                self.error_label.config(text="Max is blank, please enter a valid number.")
                return

            # If these loops are finished, and nothing is found, then there is no string and the user has entered a valid response.
            for i in num_list:
                for letter in num_list[i-1]:
                    # If there are no strings, then it will continue to check the next item in the 'num_list'
                    if re.match(valid_num, int(letter)):
                        continue
                    # If num is a string at any point, the user will be given a string error.
                    else:
                        self.error_label.config("Please enter a valid number.")


            # If min num is higher than max num, then the user will be given an error.
            if self.min > self.max:
                Start.__init__(self, "Minimum number can't be higher than maximum number.")
            else:
                # (For testing) If everything is good, then 'working' will be printed and nothing should change.
                print("Working")
                self.error_label.config(text="")
                Start.__init__(self, "")

        # If there is an error that cannot be specified, then the user will get a value error.
        except ValueError:
            print("!!!!Something happened.!!!!")