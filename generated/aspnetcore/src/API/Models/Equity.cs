/*
 * Financial Instrument Sample Polymorph
 *
 * This is the description.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: openwealth@synpulse.com
 * Generated by: https://openapi-generator.tech
 */

using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Runtime.Serialization;
using System.Text.Json;
using API.Converters;

namespace API.Models
{ 
    /// <summary>
    /// Schema of a equity instrument.
    /// </summary>
    [DataContract]
    public partial class Equity : FinancialInstrument
    {
        /// <summary>
        /// ISO2 country code.
        /// </summary>
        /// <value>ISO2 country code.</value>
        [RegularExpression("^[A-Z]{2}$")]
        [DataMember(Name="countryOfRisk", EmitDefaultValue=false)]
        public string? CountryOfRisk { get; set; }

    }
}