# Save the active graphics window to a file
ggsave(file = "plot.pdf")

# Save all future graphics to file myplots.pdf
pdf("plot", height = 5, width = 5, pointsize = 11)
# Graphics plotting
qplot(...)
qplot(...)
# Close graphics file and return to display driver
dev.off()
