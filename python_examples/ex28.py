print "1. ", True and True, "true"
print "2. ", False and True, "false"
print "3. ", 1 == 1 and 2 == 1, "false"
print "4. ", "test" == "test", "true"
print "5. ", 1 == 1 or  2 != 1, "true"
print "6. ", True or 1 == 1, "true"
print "7. ", False and 0 != 0, "false"
print "8. ", True or 1 == 1, "true"
print "9. ", "test" == "testing", "false"
print "10. ", 1 != 0 and 2 == 1, "false"
print "11. ", "test" != "testing", "true"
print "12. ", "test" == 1, "false"
print "13. ", not (True and False), "true"
print "14. ", not (1 == 1 and 0 != 1), "false"
print "15. ", not (10 == 1 or 1000 == 1000), "false"
print "16. ", not (1 != 10 or 3 == 4), "false"
print "17. ", not ("testing" == "testing" and "Zed" == "Cool Guy"), "true"
print "18. ", 1 == 1 and not ("testing" == 1 or 1 == 0), "true"
print "19. ", "chunky" == "bacon" and not (3 == 4 or 3 == 3), "false"
print "20. ", 3 == 3 and not ("testing" == "testing" or "Python" == "fun"), "false"

