package com.grupo6;

import static org.junit.Assert.assertEquals;
import org.junit.After;

import java.util.concurrent.TimeUnit;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;


public class Demo {
    
    private WebDriver driver;
    
    @Before
    public void setUp()
    {
        System.setProperty("webdriver.chrome.driver", "./Selenium/src/test/chromedriver/chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://www.google.com/");
        
    }
    
    @Test
    public void testPagina()
    {
        WebElement searchbox = driver.findElement(By.name("q"));
        searchbox.clear();
        searchbox.sendKeys("Introduccion a QS");
        searchbox.submit();
        driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS);
        assertEquals("Introduccion a QS", driver.getTitle());
    }
    
    @After
    public void tearDown()
    {
        driver.quit();
    }
}
